# Optical-Character-Recognition-using-Deep-Learning
## Character Level
First download EMNIST dataset [here](http://www.nist.gov/itl/iad/image-group/emnist-dataset) <br/>
Run **Char_rec.py**. Use the downloaded csv files for training and testing. <br/>
Edit the code as per your framework to open the csv files. I used google colab so its written accordingly.

## Word Level
1. Download IAM dataset(word images and xml file) from [here](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database)
2. Run **Images.py** to convert the images into a csv file. <br/>
3. Run **Labels.py** to extract the labels from xml file and store it in a csv file. <br/>
4. Run **Word_rec.py** to train the model using the csv files extracted above. <br/>
Edit the code as per your framework to open the csv files. I used google colab so its written accordingly.
