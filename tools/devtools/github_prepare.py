
import os
import subprocess


def main():
    # # Run Tests and create examples
    subprocess.check_call("cd ../../tests && ./run_tests.sh", shell=True)

    # Remove dependencies, create new ones
    os.remove("../../requirements.txt")
    subprocess.check_call("cd ../../ && pipreqs .", shell=True)
    with open("../../requirements.txt", "r") as f:
        data = f.read()
    data = data.split("\n")
    data.remove("skimage==0.0")
    for i, val in enumerate(data):
        if val == "webview==0.1.5":
            data[i] = "pywebview==3.2"
    with open("../../requirements.txt", "w") as f:
        f.write('\n'.join(data))
    if os.path.exists("../../tests/requirements.txt"):
        os.remove("../../tests/requirements.txt")



if __name__ == '__main__':
    main()
