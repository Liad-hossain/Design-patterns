from Design_patterns.structural_design_patterns.composite_design_pattern.example_1.Directory import (
    Directory,
)
from Design_patterns.structural_design_patterns.composite_design_pattern.example_1.File import (
    File,
)

if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("my_profile.png")
    file3 = File("file3.jpg")
    file4 = File("file4.pdf")

    # Create directories
    dir1 = Directory("Documents")
    dir2 = Directory("Pictures")
    dir3 = Directory("My Profile")

    # Add files to directories
    dir1.add(file1)
    dir1.add(file4)
    dir2.add(file3)
    dir3.add(file2)
    dir2.add(dir3)

    # Create a root directory and add subdirectories
    root = Directory("Root")
    root.add(dir1)
    root.add(dir2)

    # Display the contents of the root directory
    root.show_details()
