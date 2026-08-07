import os
import time
from services.scanner import RepoScanner
from services.llm_adapter import LLMAdapter
from services.verifier import CodeVerifier
from services.parser import CodeParser
from services.patcher import FilePatcher

def start_agent_loop():
    print("🚀 Starting CodeHarness V2 Agent...\n")
    
    target_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Point to the file you want to test
    app_file_path = os.path.join(target_dir, "app", "list_app.py")
    fixed_file_path = os.path.join(target_dir, "app", "list_app_fixed.py")
    
    scanner = RepoScanner(target_directory=target_dir)
    adapter = LLMAdapter()
    verifier = CodeVerifier(target_directory=target_dir)
    
    max_attempts = 3
    attempt = 1
    
    while attempt <= max_attempts:
        print(f"========== ATTEMPT {attempt}/{max_attempts} ==========")
        print("[1/5] Scanning repository for context...")
        context = scanner.gather_context(file_extension=".py")
        
        print("[2/5] Running test suite...")
        test_results = verifier.run_tests()
        
        if test_results["success"]:
            print("\n🎉 SUCCESS! All tests passed!")
            return
            
        print("[3/5] Tests failed. Packaging error logs for AI...")
        
        system_prompt = (
            "You are an autonomous AI coding agent. Review the provided code context "
            "and the failing test output. Find the bug. "
            "Reply with ONLY the complete, fixed Python code wrapped in a ```python ``` block. "
            "Do not include any explanations or conversational text."
        )
        
        user_prompt = (
            f"--- CODE CONTEXT ---\n{context}\n\n"
            f"--- TEST ERRORS ---\n{test_results['output']}\n\n"
            "Fix the bug and provide the updated file."
        )
        
        print("[4/5] Awaiting AI fix...")
        ai_response = adapter.generate_patch(system_prompt, user_prompt)
        
        print("[5/5] Extracting code and generating new file...")
        clean_code = CodeParser.extract_code(ai_response)
        
        if clean_code:
            FilePatcher.apply_patch(fixed_file_path, clean_code)
            print(f"\n✅ Patch applied! Saved to: list_app_fixed.py")
            break
        else:
            print("Failed to extract code from AI response. Retrying...\n")
            
        attempt += 1
        time.sleep(2)

if __name__ == "__main__":
    start_agent_loop()