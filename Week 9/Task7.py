import sys
import os
def show_help() -> None:
    print("Print usage instructions")
    print("Invalid amount of arguments.")
    print("[USAGE] python {} src_file dst_file".format(sys.argv[0]))
def copy_file(Src_file: str, Dst_file: str) -> None:
    print(f"Source file : {Src_file}")
    print(f"Destination file : {Dst_file}")
    print(f"Copying file '{Src_file}' to '{Dst_file}'")
    proceed = True
    if os.path.exists(Dst_file):
        answer = input("Your destination file alreay exist. Do you want to overwrite? (y/n)").lower()
        if answer != "y":
            print("Copy cancelled by user.")
            proceed = False
    if proceed:
        try:
            with open(Src_file, "r") as f:
                content = f.read()
            with open(Dst_file, "w") as file:
                file.write(content)
        except FileNotFoundError:
            print(f'Error: Source file "{Src_file}" does not exist.')
            sys.exit(-1)
        except Exception as e:
            print(f"File is not copying due to error {e}")
            sys.exit(-1)


            
    

def main() -> None:
    if len(sys.argv) != 3:
        show_help()
        sys.exit(1)
    Src_file = sys.argv[1]
    Dst_file = sys.argv[2]
    print("Program starting")
    copy_file(Src_file, Dst_file)
    print("Program ending")
    



if __name__ == "__main__":
    main()
    
# python "Week 9\Task7.py" "Week 9\A9_T7_D2.txt" "Week 9\A9_T7_F1.txt"
