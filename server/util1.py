import os

def

def get_b64_test_image_for_virat():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'b64.txt')
    with open(file_path) as f:
        return f.read()
    
if __name__ == '__main__':
    get_b64_test_image_for_virat()