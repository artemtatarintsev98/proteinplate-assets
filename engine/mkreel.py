import subprocess, random, glob, os
def make(rid, pngs, out):
    mus=random.choice(sorted(glob.glob("music/*.mp3")))
    start=random.randint(0,40)
    z="zoompan=z='min(zoom+0.0009,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=120:s=1080x1920:fps=30"
    fc=(f"[0]scale=1188:2112,{z},setsar=1[a];[1]scale=1080:1920,fps=30,setsar=1[b];[2]scale=1080:1920,fps=30,setsar=1[c];[3]scale=1080:1920,fps=30,setsar=1[e];"
        "[a][b]xfade=transition=slideleft:duration=0.4:offset=3.6[ab];[ab][c]xfade=transition=slideleft:duration=0.4:offset=7.2[abc];"
        "[abc][e]xfade=transition=fade:duration=0.4:offset=11.8[v];[4:a]afade=t=in:d=0.5,afade=t=out:st=14.3:d=0.8,volume=0.8[au]")
    cmd=["ffmpeg","-y","-loglevel","error",
         "-loop","1","-t","4","-i",pngs[0],"-loop","1","-t","4","-i",pngs[1],"-loop","1","-t","5","-i",pngs[2],"-loop","1","-t","3.5","-i",pngs[3],
         "-ss",str(start),"-i",mus,"-filter_complex",fc,"-map","[v]","-map","[au]","-t","15.1",
         "-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-movflags","+faststart",out]
    subprocess.run(cmd,check=True)
    return os.path.basename(mus)
