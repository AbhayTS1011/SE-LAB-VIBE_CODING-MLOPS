import subprocess

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    print("=== DVC Data Versioning Demo ===" )
    print("Current data.csv content:")
    with open("data.csv", "r") as f:
        print(f.read())
    
    print("\nTo switch to version 1 (v1.0):")
    print("1. git checkout v1.0")
    print("2. dvc checkout")
    print("Try running these commands in your terminal!")
