import csv
import logging
import xml.etree.ElementTree as ET
import unittest
import os

# Defined the required headers for writing into the CSV file 
HEADERS = [
    "FinInstrmGnlAttrbts_Id",
    "FinInstrmGnlAttrbts_FullNm",
    "FinInstrmGnlAttrbts_ClssfctnTp",
    "FinInstrmGnlAttrbts_CmmdtyDerivInd",
    "FinInstrmGnlAttrbts_NtnlCcy",
    "Issr"
]
class TestXMLtoCSV_Conversion(unittest.TestCase):
    """
    A class for testing the conversion of XML to CSV files.
    """

    def setUp(self):
        """
        Set up the path of the input XML file and to the output directory.
        """
        self.xml_file = ("A:\\Developments and Projects\\Python Projects\\DLTINS_20210117_01of01.xml")
        self.csv_file = "output_FINAL.csv"
    
    def test_xml_to_cs(self):
        """
        Test that the XML file is correctly converted to a CSV file.
        """
        # Check that the CSV file was created
        self.assertTrue(os.path.exists(self.csv_file))
        
        # Check that the CSV file has data in it
        with open(self.csv_file, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            self.assertGreater(len(list(reader)), 0)

def main():
    # Configuring the standard logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    """
    Extracts data from an XML file and writes it to a CSV file.
    """
    # Creating a CSV file and writing the mentioned headers to it
    with open("output_FINAL.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(HEADERS)
        
        # Parse the XML file
        """Try and Catch Block for Checking 'ParseError' """
        try:
            tree = ET.parse("A:\Developments and Projects\Python Projects\DLTINS_20210117_01of01.xml")
            root = tree.getroot()
        except ET.ParseError as e:
            logging.exception("Error parsing XML file")
            return
        
        # Loop through each element in the XML file and extract the relevant data
        for TermntdRcrd in tree.iter("TermntdRcrd"):
            FinInstrmGnlAttrbts = TermntdRcrd.find("FinInstrmGnlAttrbts")
            if FinInstrmGnlAttrbts is not None:
                FinInstrmGnlAttrbts_Id = FinInstrmGnlAttrbts.find("Id").text
                FinInstrmGnlAttrbts_FullNm = FinInstrmGnlAttrbts.find("FullNm").text
                FinInstrmGnlAttrbts_ClssfctnTp = FinInstrmGnlAttrbts.find("ClssfctnTp").text
                FinInstrmGnlAttrbts_CmmdtyDerivInd = FinInstrmGnlAttrbts.find("CmmdtyDerivInd").text
                FinInstrmGnlAttrbts_NtnlCcy = FinInstrmGnlAttrbts.find("NtnlCcy").text
            else:
                FinInstrmGnlAttrbts_Id = ""
                FinInstrmGnlAttrbts_FullNm = ""
                FinInstrmGnlAttrbts_ClssfctnTp = ""
                FinInstrmGnlAttrbts_CmmdtyDerivInd = ""
                FinInstrmGnlAttrbts_NtnlCcy = ""
            
            Issr = TermntdRcrd.find("Issr").text
            # Assignning the gathered data to the data variable
            data = [
                FinInstrmGnlAttrbts_Id,
                FinInstrmGnlAttrbts_FullNm,
                FinInstrmGnlAttrbts_ClssfctnTp,
                FinInstrmGnlAttrbts_CmmdtyDerivInd,
                FinInstrmGnlAttrbts_NtnlCcy,
                Issr
            ]
            
            # Write the data to the CSV file
            writer.writerow(data)
        logging.info("Wrote All Rows to the CSV file: ")

if __name__ == "__main__":
    main()
    # Running all the tests 
    unittest.main()
