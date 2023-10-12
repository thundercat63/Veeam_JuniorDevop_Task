#Hazal_Yurtbak_2023_october
#codes for a Junior Developer position in Veeam Software
#code entirely belongs to me.

#First, we import the necessary Python modules:
import os
import shutil
import logging
import time
import argparse
import hashlib

#We define a function called "primal_function". This function sets the configurations and format for logging
def primal_function(ent_file):
    logging.basicConfig(filename=ent_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    remoter = logging.StreamHandler()
    remoter.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    remoter.setFormatter(formatter)
    logging.getLogger('').addHandler(remoter)

#A function named calculate_md5 is defined. This function calculates the MD5 hash of a file:
def calculate_md5(way_of_file):
    """Calculate md5 and return the MD5 hash of a file."""
    md5_hesap = hashlib.md5()
    with open(way_of_file, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            md5_hesap.update(data)
    return md5_hesap.hexdigest()

#We define the main synchronization function called synchronize_folders:
def synchronization_folders(folder_source, folder_replica, ent_file, interval):
    try:
        # Ensure source folder exists
        if not os.path.exists(folder_source):
            logging.error(f"Source folder '{folder_source}' does not exist.")
            return

        # Ensure replica folder exists; if not, create it
        if not os.path.exists(folder_replica):
            os.makedirs(folder_replica)
            logging.info(f"Replica folder '{folder_replica}' created.")

        # Initialize logging
        primal_function(ent_file)

#We start an infinite loop because we want the synchronization to run at certain intervals:
        while True:
            #We start a loop to remove all files and folders from the copy folder:
            for thing in os.listdir(folder_replica):
                replica_thing = os.path.join(folder_replica, thing)
                if os.path.isdir(replica_thing):
                    shutil.rmtree(replica_thing)
                    logging.info(f"Directory '{thing}' removed from replica folder.")
                else:
                    os.remove(replica_thing)
                    logging.info(f"File '{thing}' removed from replica folder.")

            #Next, we start a loop to copy all the contents from the source folder to the copy folder:
            for thing in os.listdir(folder_source):
                source_thing = os.path.join(folder_source, thing)
                replica_thing = os.path.join(folder_replica, thing)
                #If the file or folder source is a folder, we copy this folder to the copy folder:
                if os.path.isdir(source_thing):
                    shutil.copytree(source_thing, replica_thing)
                    logging.info(f"Directory '{thing}' copied to replica folder.")
                #If it is a file, we copy this file to the copy folder:
                else:
                    shutil.copy2(source_thing, replica_thing)
                    logging.info(f"File '{thing}' copied to replica folder.")
            #When the synchronization process is completed, we record a log message:
            logging.info("Synchronization is succesful!!!!")

            # We wait until the specified interval:
            time.sleep(interval)
    #In case of any error we record an error message:
    except Exception as e:
        logging.error(f"upppss! an error!!!!: {str(e)}")

#This codes are used to folders from the source folder to the copy folder. 
# The synchronization process runs automatically at certain intervals and the operations are recorded 
# in the log file and console output.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Folder Synchronization")
    parser.add_argument("folder_source", help="Path to the source folder")
    parser.add_argument("folder_replica", help="Path to the replica folder")
    parser.add_argument("ent_file", help="Path to the log file")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")

    args = parser.parse_args()
    
    synchronization_folders(args.folder_source, args.folder_replica, args.ent_file, args.interval)


    #I am glad that you read my codes. I am currently working on python and java.
    #I am a hardworking person and curious to learn. I would be very happy if you would like to get to know me better. 
    # I believe this job is exactly for me.