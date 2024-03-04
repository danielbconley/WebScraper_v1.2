import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")

def main():
    scripts_to_run = [
        "web_scrape_tts.py",
        "generate_video.py",
        "split_video.py"
    ]

    for script in scripts_to_run:
        run_script(script)

if __name__ == "__main__":
    main()
