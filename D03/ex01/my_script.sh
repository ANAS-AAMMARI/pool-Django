
#!/bin/bash

# Display pip version
pip show pip | grep Version

# Define the installation directory
install_dir="local_lib"

# Remove the directory if it exists
rm -rf $install_dir

# Create the directory
mkdir $install_dir

cd $install_dir
# Install the library in editable mode and write logs to a .log file
pip install -e git+https://github.com/jaraco/path.py.git#egg=path --log ../install.log 

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "path.py installed successfully."
    # Run the Python program
    cd ..
    python3 my_program.py
else
    echo "path.py installation failed."
fi

# #!/bin/bash

# # Display pip version
# pip show pip | grep Version

# # Define the installation directory
# install_dir="local_lib"

# # Remove the directory if it exists
# rm -rf $install_dir

# # Clone the path.py repo into the directory
# git clone https://github.com/jaraco/path.py.git $install_dir > install.log

# # Change to the directory
# cd $install_dir

# # Install the library
# pip install -e . >> ../install.log

# # Execute the Python program
# python3 ../my_program.py
