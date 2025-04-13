import subprocess
import openai

def run_with_auto_fix(file_path):
    try:
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        if result.returncode != 0:
            error_msg = result.stderr
            print("⚠️ Error detected. Asking AI to fix it...")
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert Python bug fixer."},
                    {"role": "user", "content": f"The following code has an error: {error_msg}\nPlease provide the fixed code."}
                ]
            )
            print("🔧 Suggested fix:\n", response.choices[0].message.content)
            # Optional: write fixed code to file
        else:
            print("✅ No errors. Output:\n", result.stdout)
    except Exception as e:
        print("Auto-fix failed:", e)
