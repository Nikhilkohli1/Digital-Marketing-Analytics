

xsv sample 100000 Dataset_Cleaned_final

xsv slice -i 5 sampled_data5.csv | xsv flatten 
 
xsv frequency sampled_data5.csv

xsv headers sampled_data5.csv

xsv stats sampled_data5.csv | xsv table

xsv slice sampled_data5.csv -s 1 -e 11 | xsv table
