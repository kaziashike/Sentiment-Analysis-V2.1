
import os
from transcribe import transcribe_audio
from analyze import analyze_text

def Processing(audio_file):
    if not os.path.exists(audio_file):
        print("The specified audio file does not exist.")
        return
    
    #Transcribe the audio file
    transcription = transcribe_audio(audio_file)
    print('transcription done')
   
    
    if transcription:
        # Analyze the transcription
        print("starting analysis.")
        analysis_result = analyze_text(transcription)
        return(analysis_result)
       
    else:
        return("Transcription failed.")
print(Processing('downloads\\20250124-075737_AFS_INBO_AFS_Future_School_Tamimul_01870406558-all.mp3'))



