import os
import string
import socket

def main():
   
    with open("/home/output/result.txt", "w") as result_file:
        
        # List all files in the /home/data directory
        data_dir = "/home/data"
        file_names = os.listdir(data_dir)
        result_file.write(f"Files in {data_dir}:\n")
        for file_name in file_names:
            result_file.write(f"{file_name}\n")
        

        limerick_file_path = os.path.join(data_dir, "Limerick.txt")
        with open(limerick_file_path, "r") as limerick_file:
            limerick_words = limerick_file.read().split()
            limerick_word_count = len(limerick_words)
            result_file.write(f"\nNumber of words in Limerick: {limerick_word_count}")
            
        if_file_path = os.path.join(data_dir, "IF.txt")
        with open(if_file_path, "r") as if_file:
            if_words = if_file.read().split()
            if_words = [word.translate(str.maketrans('', '', string.punctuation)).capitalize() for word in if_words]
            if_word_count = len(if_words)
            result_file.write(f"\nNumber of words in IF: {if_word_count}")
        
        total_word_count = limerick_word_count + if_word_count
        result_file.write(f"\nTotal number of words in both files: {total_word_count}")
        

        word_counts = {}
        for word in if_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        result_file.write("\nTop 3 words with maximum number of counts in IF.txt:\n")
        for word, count in top_words:
            result_file.write(f"{word} - {count}\n")
        

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        result_file.write(f"\nMachine IP Address is: {ip_address}")
    

    with open("/home/output/result.txt", "r") as result_file:
        print(result_file.read())

if __name__ == "__main__":
    main()
