import pandas as pd
import io

csv_data = """year,constituency,district,total_voters,votes_polled,turnout_pct,winning_party,winning_vote_pct,runnerup_vote_pct,margin_pct,urban_index,party_change_freq,anti_incumbency_score,new_party_vote_pct
2021,Vaniyambadi,Tirupathur,238510,183421,76.90,AIADMK,46.69,44.09,2.60,0.4,3,1.2,5.96
2021,Vanur,Villupuram,226539,180845,79.83,AIADMK,50.99,38.98,12.01,0.2,1,14.2,4.75
2021,Vasudevanallur,Tenkasi,222117,173710,78.21,DMK,39.60,38.20,1.40,0.2,2,4.8,9.6
2021,Vedaranyam,Nagapattinam,184292,157387,85.40,AIADMK,50.00,42.20,7.80,0.2,2,8.6,5.8
2021,Veerapandi,Salem,222474,191772,86.20,AIADMK,50.20,41.30,8.90,0.4,2,3.1,4.4
2021,Velachery,Chennai,314537,174972,55.63,INC,39.15,36.66,2.49,0.9,2,0.8,21.2
2021,Vellore,Vellore,254345,174136,68.46,DMK,46.10,41.29,4.81,0.8,2,3.4,5.2
2021,Vilathikulam,Thoothukudi,209256,166133,79.39,DMK,54.40,31.20,23.20,0.1,3,15.2,7.1
2021,Villivakkam,Chennai,258901,145321,56.13,DMK,52.40,31.20,21.20,0.9,2,8.4,12.5
2021,Villupuram,Villupuram,262068,203890,77.80,DMK,50.16,42.87,7.29,0.6,2,13.4,3.13
2021,Virudhunagar,Virudhunagar,212379,160147,75.40,DMK,48.60,36.30,12.30,0.5,1,9.8,8.9
2021,Viralimalai,Pudukkottai,195148,167512,85.84,AIADMK,52.90,40.70,12.20,0.2,0,1.1,3.6
2021,Vikravandi,Villupuram,234365,193397,82.52,DMK,48.41,43.47,4.94,0.2,3,4.3,4.1
2021,Vriddhachalam,Cuddalore,252844,196734,77.81,INC,39.17,38.73,0.44,0.3,3,-0.1,17.5
2016,Vaniyambadi,Vellore,223883,170864,76.32,AIADMK,46.21,37.71,8.50,0.4,2,8.4,7.2
2016,Vanur,Villupuram,220293,172998,78.53,AIADMK,44.11,38.20,5.91,0.2,1,7.2,10.1
2016,Vasudevanallur,Tirunelveli,225946,167117,73.96,AIADMK,45.60,34.38,11.22,0.2,1,6.8,11.5
2016,Vedaranyam,Nagapattinam,180886,145394,80.38,AIADMK,52.01,36.19,15.82,0.2,1,12.1,8.4
2016,Veerapandi,Salem,236664,211102,89.20,AIADMK,47.20,40.34,6.86,0.4,1,9.2,6.5
2016,Velachery,Chennai,296329,171297,57.81,DMK,39.96,34.78,5.18,0.9,1,13.5,15.2
2016,Vellore,Vellore,235410,158430,67.30,DMK,44.50,37.02,7.48,0.8,1,4.2,9.8
2016,Vilathikulam,Thoothukudi,209256,158485,75.74,AIADMK,44.50,32.69,11.81,0.1,2,5.4,12.3
2016,Villivakkam,Chennai,252292,146675,58.14,DMK,44.11,37.75,6.36,0.9,1,8.9,11.2
2016,Villupuram,Villupuram,248430,195410,78.66,AIADMK,40.89,31.02,9.87,0.6,1,11.2,14.5
2016,Virudhunagar,Virudhunagar,205887,150512,73.10,DMK,43.20,41.29,1.91,0.5,1,2.1,10.6
2016,Viralimalai,Pudukkottai,191954,169873,88.50,AIADMK,47.50,42.53,4.97,0.2,0,5.2,5.8
2016,Vikravandi,Villupuram,212710,174185,81.89,DMK,36.50,32.53,3.97,0.2,2,4.8,15.6
2016,Vriddhachalam,Cuddalore,242150,188450,77.82,AIADMK,42.40,35.09,7.31,0.3,2,6.5,18.4
2011,Vaniyambadi,Vellore,175432,135421,77.19,AIADMK,54.65,42.29,12.36,0.4,1,15.2,1.7
2011,Vanur,Villupuram,204212,165410,81.00,AIADMK,55.20,38.40,16.80,0.2,0,18.4,0.5
2011,Vasudevanallur,Tirunelveli,198421,155432,78.33,AIADMK,56.10,38.20,17.90,0.2,0,14.2,1.2
2011,Vedaranyam,Nagapattinam,168430,142310,84.50,AIADMK,51.20,44.50,6.70,0.2,0,11.5,0.8
2011,Veerapandi,Salem,215432,192450,89.33,AIADMK,52.10,43.50,8.60,0.4,0,10.2,1.5
2011,Velachery,Chennai,227204,152364,67.06,AIADMK,53.91,33.10,20.81,0.9,0,53.9,9.5
2011,Vellore,Vellore,210450,155430,73.85,DMK,48.40,41.10,7.30,0.8,0,2.1,8.5
2011,Vilathikulam,Thoothukudi,185410,145321,78.37,AIADMK,58.40,34.20,24.20,0.1,1,12.5,2.4
2011,Villivakkam,Chennai,212345,145432,68.48,AIADMK,53.20,38.40,14.80,0.9,0,11.2,6.1
2011,Villupuram,Villupuram,209392,173050,82.64,AIADMK,52.18,45.19,6.99,0.6,0,5.3,0.6
2011,Virudhunagar,Virudhunagar,185430,145321,78.37,DMK,46.50,42.10,4.40,0.5,0,3.2,8.4
2011,Viralimalai,Pudukkottai,175432,152341,86.84,AIADMK,58.40,34.20,24.20,0.2,0,18.4,2.5
2011,Vikravandi,Villupuram,195432,165432,84.65,CPI(M),48.40,41.20,7.20,0.2,1,9.8,2.4
2011,Vriddhachalam,Cuddalore,215432,175432,81.43,DMDK,48.60,36.50,12.10,0.3,1,15.4,48.6
2006,Vaniyambadi,Vellore,165432,112435,67.96,DMK,53.16,34.75,18.41,0.4,0,4.9,7.5
2006,Vanur,Villupuram,195432,145432,74.41,DMK,48.20,44.50,3.70,0.2,0,2.1,8.4
2006,Vasudevanallur,Tirunelveli,185432,135432,73.04,MDMK,46.50,42.10,4.40,0.2,0,5.4,46.5
2006,Vedaranyam,Nagapattinam,154321,125432,81.28,DMK,49.50,42.40,7.10,0.2,0,3.2,6.4
2006,Veerapandi,Salem,205432,185432,90.26,DMK,52.40,41.20,11.20,0.4,0,8.4,2.5
2006,Vellore,Vellore,195410,135420,69.30,DMK,45.20,39.40,5.80,0.8,0,6.4,12.4
2006,Vilathikulam,Thoothukudi,175432,125432,71.49,DMK,46.50,44.10,2.40,0.1,0,3.2,5.4
2006,Villivakkam,Chennai,285432,165432,57.96,DMK,48.50,42.10,6.40,0.9,0,5.2,8.4
2006,Villupuram,Villupuram,195432,152432,78.00,DMK,49.20,45.10,4.10,0.6,0,2.1,3.4
2006,Virudhunagar,Virudhunagar,175432,125432,71.49,MDMK,44.20,42.10,2.10,0.5,0,4.5,44.2
2006,Vriddhachalam,Cuddalore,185432,142341,76.76,DMDK,40.42,31.34,9.08,0.3,0,40.4,40.4
2001,Vaniyambadi,Vellore,154321,95432,61.84,IND,48.26,37.63,10.63,0.4,0,48.2,6.8
2001,Vanur,Villupuram,185432,125432,67.64,AIADMK,52.40,41.20,11.20,0.2,0,12.5,1.2
2001,Vasudevanallur,Tirunelveli,175432,115432,65.79,AIADMK,54.20,38.40,15.80,0.2,0,14.5,0.8
2001,Vedaranyam,Nagapattinam,145432,115432,79.37,AIADMK,51.20,44.50,6.70,0.2,0,10.5,1.4
2001,Veerapandi,Salem,195432,165432,84.65,AIADMK,55.40,38.40,17.00,0.4,0,15.2,0.5
2001,Vellore,Vellore,175410,105430,60.10,AIADMK,52.40,42.10,10.30,0.8,0,0.0,1.2
2001,Vilathikulam,Thoothukudi,165432,115432,69.77,AIADMK,51.20,45.40,5.80,0.1,0,8.4,1.4
2001,Villivakkam,Chennai,245432,125432,51.11,TMC(M),52.40,41.20,11.20,0.9,0,14.5,2.4
2001,Villupuram,Villupuram,195432,132451,67.77,DMK,47.45,45.86,1.59,0.6,0,-10.8,2.1
2001,Virudhunagar,Virudhunagar,165432,115432,69.77,AIADMK,52.40,41.20,11.20,0.5,0,12.1,1.5
2001,Vriddhachalam,Cuddalore,175410,105430,60.10,PMK,50.13,44.95,5.18,0.3,0,12.7,1.2"""

# Reading into DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Script logic for full output
def generate_full_report(dataframe):
    print("--- Tamil Nadu Assembly Election Data Analysis (2001-2021) ---")
    print(f"Total Rows: {len(dataframe)}")
    print("-" * 60)
    # Group by Year and Constituency
    for year in sorted(dataframe['year'].unique(), reverse=True):
        print(f"\\nElection Year: {year}")
        print(dataframe[dataframe['year'] == year][['constituency', 'winning_party', 'margin_pct', 'turnout_pct']])
    
    # Export to local file
    dataframe.to_csv("TN_Election_Consolidated_2001_2021.csv", index=False)
    print("\\nSuccess: Data exported to 'TN_Election_Consolidated_2001_2021.csv'")

generate_full_report(df)