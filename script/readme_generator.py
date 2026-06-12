import os
import sys
import google.generativeai as genai

def setup_api():
    """Configures the Gemini API."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("🔑 Gemini API Key not found in environment variables.")
        api_key = input("Please paste your Gemini API Key: ").strip()
        if not api_key:
            print("❌ API Key is required to run this script.")
            sys.exit(1)
    genai.configure(api_key=api_key)

def main():
    setup_api()
    
    # Using gemini-1.5-flash for fast, high-quality text generation
    model_name = 'gemini-1.5-flash'
    
    # System instructions to guarantee an elite, copyable GitHub README structure
    system_instruction = (
        "You are an expert technical writer and open-source maintainer. Your task is to generate "
        "exceptionally professional GitHub README.md files. Use clean Markdown formatting, industry-standard "
        "sections (Badges, Features, Architecture, Installation, Usage, Contributing, License), and clear code blocks. "
        "When responding, provide ONLY the raw Markdown content. Do not wrap your entire response in markdown code blocks (```markdown ... ```)—just output the direct markdown syntax so it can be saved cleanly into a file."
    )
    
    print("\n==================================================")
    print("🤖 Welcome to the Professional AI README Generator")
    print("==================================================\n")
    
    # Gather initial project details
    project_name = input("📁 Enter Project Name: ").strip()
    project_desc = input("📝 Short Project Description (What does it do?): ").strip()
    tech_stack = input("🛠️ Tech Stack / Dependencies (comma-separated): ").strip()
    
    initial_prompt = (
        f"Generate a highly professional GitHub README.md for a project named '{project_name}'.\n"
        f"Description: {project_desc}\n"
        f"Tech Stack: {tech_stack}\n"
        f"Make sure it includes professional placeholders, clear sections, installation commands, and usage instructions."
    )
    
    print("\n⏳ Fabricating your premium README architecture...")
    
    # Initialize a chat session to maintain context for revisions
    model = genai.GenerativeModel(model_name=model_name, system_instruction=system_instruction)
    chat = model.start_chat(history=[])
    
    # Generate the initial README
    response = chat.send_message(initial_prompt)
    readme_content = response.text
    
    # Save to file immediately
    filename = "README.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    print(f"\n✅ Fresh README.md successfully created in this directory!")
    print("--------------------------------------------------")
    print(readme_content[:800] + "\n... [Truncated for preview] ...")
    print("--------------------------------------------------")
    
    # Interactive Revision Loop
    while True:
        print("\n🔄 Options: Type your refinement feedback (e.g., 'make it more professional', 'add a configuration section')")
        print("   Or type 'exit' if you love the current version.")
        feedback = input("\n💬 Your feedback: ").strip()
        
        if feedback.lower() == 'exit':
            print(f"\n🎉 Awesome! Your final professional README is saved completely inside '{filename}'.")
            break
            
        if not feedback:
            continue
            
        print("⏳ Polishing and restructuring the README based on your instructions...")
        
        # Send the user's tweak to the chat context
        refine_prompt = f"Modify the current README based on this feedback: {feedback}. Output the entire updated README text."
        response = chat.send_message(refine_prompt)
        readme_content = response.text
        
        # Overwrite file with updated content
        with open(filename, "w", encoding="utf-8") as f:
            f.write(readme_content)
            
        print(f"\n✨ README.md updated successfully with your changes!")
        print("--------------------------------------------------")
        print(readme_content[:500] + "\n... [Truncated for preview] ...")
        print("--------------------------------------------------")

if __name__ == "__main__":
    main()
