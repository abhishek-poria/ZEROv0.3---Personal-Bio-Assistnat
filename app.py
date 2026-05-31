from Bio.Seq import Seq
import streamlit as st

#---MAIN MENU---
st.title("ZEROv0.3 : Personal Bio Assistant")
st.subheader("I'm beta version of ZERO")
name = st.text_input("Your Good Name Please?").capitalize()
if name :
    st.write(f"Welcome {name}")
    choice = st.selectbox("What you want me to do?",["DNA sequence length calculator",
                                            "DNA slicing", "Perform Central Dogma", 
                                            "GC content calculator", "Pyrimidine and Purine calculator",
                                             ])
    
    if choice == "DNA sequence length calculator":
        my_dna = st.text_input("Enter DNA sequence here :").upper().strip()
        if not all(base in "ATCG" for base in my_dna):
            st.write("INVALID SEQUENCE : 404")
            st.write("Enter a valid DNA sequence")
        else :
            if my_dna :
                st.write(f"length of this sequence is:{len(my_dna)} nucleotide")
           
    elif choice == "DNA slicing":
        ask_dna = st.text_input("Enter DNA sequence here :").upper().strip()
        if not all(base in "ATCG" for base in ask_dna):
            st.write("INVALID SEQUENCE : 404")
            st.write("Enter a valid DNA sequence")
        else :
            if ask_dna:
                chop = [ask_dna[i:i+3] for i in range(0,len(ask_dna),3)]
                st.write(f"Newly formed codons are : {chop}")
            
    elif choice == "Perform Central Dogma" :
        st.write("What do you want me to do?")
        dna_2_rna = st.checkbox("Transcription")
        rna_2_protein = st.checkbox("Translation")
        rna_2_dna = st.checkbox("Reverse Transcription")
        dna_2_dna = st.checkbox("Replication")
        
        if dna_2_rna :
            choice_dna = Seq(st.text_input("Enter DNA sequence here :")).upper().strip()
            if not all(base in "ATCG" for base in choice_dna):
               st.write("INVALID SEQUENCE : 404")
               st.write("Enter a valid DNA sequence")
            else:
                if dna_2_rna :
                    rna = choice_dna.transcribe()
                    st.write(f"Your new RNA sequence is : {rna}")
                
        elif rna_2_protein :
            choice_rna = Seq(st.text_input("Enter RNA sequence here :")).upper().strip()
            if not all(base in "AUCG" for base in choice_rna):
               st.write("INVALID SEQUENCE : 404")
               st.write("Enter a valid RNA sequence")
            else :
                if rna_2_protein :
                    protein = choice_rna.translate()
                    st.write(f"Your new protein sequence is : {protein}")
                
        elif rna_2_dna :
            choice_rna2 = Seq(st.text_input("Enter RNA sequence here :")).upper().strip()
            if not all(base in "AUCG" for base in choice_rna2):
               st.write("INVALID SEQUENCE : 404")
               st.write("Enter a valid RNA sequence")
            else :
                if rna_2_dna :
                    new_dna = choice_rna2.back_transcribe()
                    st.write(f"Your new DNA sequence is : {new_dna}")   

        elif dna_2_dna :
            user_dna = Seq(st.text_input("Enter DNA sequence here :")).upper().strip()
            if not all(base in "ATCG" for base in user_dna):
               st.write("INVALID SEQUENCE : 404")
               st.write("Enter a valid DNA sequence")
            else:
                if dna_2_dna :
                    new_dna1 = user_dna.complement()
                    st.write(f"Your new DNA complementry sequence is : {new_dna1}")
    
    elif choice == "GC content calculator" :
        DNA_GC = Seq(st.text_input("Enter DNA sequence here :")).upper().strip()
        if not all(base in "ATCG" for base in DNA_GC):
            st.write("INVALID SEQUENCE : 404")
            st.write("Enter a valid DNA sequence")
        else:
            if DNA_GC :
                G_count = DNA_GC.count("G")
                C_count = DNA_GC.count("C")
                GC_count = (G_count + C_count)/(len(DNA_GC))*100
                st.write(f"{GC_count:.2f}%")
    elif choice == "Pyrimidine and Purine calculator" :
        st.write("Please check sidebar navigation for this operation. Thank You!")
        side = st.sidebar.selectbox("Enter your choice:", ["Pyrimidine","Purine"])
        if side == "Pyrimidine" :
            dna_rna_seq = Seq(st.sidebar.text_input("Enter you DNA/RNA sequence here:")).upper().strip()
            if dna_rna_seq :
                T_count = dna_rna_seq.count("T")
                C_count = dna_rna_seq.count("C")
                U_count = dna_rna_seq.count("U")
                TUC_count = (T_count + C_count + U_count)/(len(dna_rna_seq))*100
                st.sidebar.write(f"{TUC_count:.2f}%")
        
        elif side == "Purine" :
            dna_rna_seq1 = Seq(st.sidebar.text_input("Enter you DNA/RNA sequence here:")).upper().strip()
            if dna_rna_seq1 :
                A_count = dna_rna_seq1.count("A")
                G_count = dna_rna_seq1.count("G")
                AG_count = (A_count + G_count)/(len(dna_rna_seq1))*100
                st.sidebar.write(f"{AG_count:.2f}%")

        
info = st.caption("*ZER0v0.3 is underdeveloping tool and can make mistakes. Sorry for inconvenience, if any. ")

                


            
                     



    
