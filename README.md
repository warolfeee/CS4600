**STEPS TO CREATE A CNN MODEL FOR RECOGNIZING A SPECIFIC BIRD CALL:**  
1. Download the recording JSON from the xeno-canto API  
	- URL to the xeno-canto website: *https://xeno-canto.org*  
	- wget https://www.xeno-canto.org/api/2/recordings?query=northern+raven  
	*northern raven can be changed to what ever bird the user would like to use*  
  
	- The file can be renamed to fit the needs of the user, but open the file and see how many pages that bird species has (it will be the value of numPages in the JSON object).  
	- If all of the recordings of the bird are needed, add the page number to the url and consecutively run the wget command. *(wget https://xeno-canto.org/api/2/recordings?query=northern+raven&page=2)*  
	- In the JSON object there is also a recording id and parseBirdId.py can be used to get the bird id for downloading the recordings. (The file parameter in the JSON object could also be used.)  
	- `parseBirdId.py < "firstBirdIds.txt"` This will start the script and name the file that will hold the bird IDs.  
	- The script will not run until you type in the file name holding the JSON object and be sure to wrap "" around the file name.  
	- Use the following command to download all of the mp3 files `for line in /`cat firstBirdIds.txt/`; do wget https://xeno-canto.org/${line}/download; done`  
  
2. Convert the .mp3 audio recordings to .wav files  
	- Wav files are easier to work with when converting audio to images so run the following command to convert the files to wav:  `for file in download*; do ffmpeg -i ${file} ./nraven${file##*.}.wav; done`  
	- Since all the files are named with the format of download.55, the previoud command will gather all the download files in the current directory and name them according to their number after the .  
  
3. Covert the .wav files into spectrograms  
	-Use the spectro.py file to convert the wav files into spectrograms to feed to the CNN. **Make sure to change in the spectro.py file: audio_fpath to be the path of your recordings, plt.savefig() to have the name you want for your spectrograms**    
  
3. Covert the .wav files into spectrograms  
	-Use the spectro.py file to convert the wav files into spectrograms to feed to the CNN. `python spectro.py`  
	**Make sure to change in the spectro.py file: audio_fpath to be the path of your recordings and plt.savefig() to have the name you want for your spectrograms**  
  
4. Manually sort through the photos in order to seperate 'background noise' and the call of the bird you are working with. Put the photos in different directories.  
  
5. Use numpyArray.py in order to properly grayscale, resize, and label the images. `python numpyArray.py`  
	**Make sure to change in numpyArray.py: DATADIR to the path of your directory, CATEGORIES to be the categories you are using and IMG_SIZE to be the size you want to work with**  
  
6. Use the tensor.py in order to build and train the CNN model. `python tensor.py`  
  
 **GOOD LUCK!**


