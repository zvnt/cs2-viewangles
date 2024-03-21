import subprocess
import time
import os
import winreg
import socket
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('{}')

def getpath(key_path, value_name):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            value, _ = winreg.QueryValueEx(key, value_name)
            return value
    except WindowsError:
        return None
    
def config(cs2path):
    viewangles_commands = """
log_flags LOADING +DoNotEcho;log_flags General +DoNotEcho;log_flags Assert +DoNotEcho;log_flags Console +DoNotEcho;log_flags Developer +DoNotEcho;log_flags DeveloperConsole +DoNotEcho;log_flags DeveloperVerbose +DoNotEcho;log_flags Symbols +DoNotEcho;log_flags ToolsStallMonitor +DoNotEcho;log_flags Stack +DoNotEcho;log_flags EntityLoadUnserialize +DoNotEcho;log_flags EntitySystem +DoNotEcho;log_flags VScript +DoNotEcho;log_flags VScriptDbg +DoNotEcho;log_flags Demo +DoNotEcho;log_flags InstantReplay +DoNotEcho;log_flags RCon +DoNotEcho;log_flags Steam +DoNotEcho;log_flags ClockDrift +DoNotEcho;log_flags Shooting +DoNotEcho;log_flags Server +DoNotEcho;log_flags SpawnGroup +DoNotEcho;log_flags SignonState +DoNotEcho;log_flags Movie +DoNotEcho;log_flags ServerLog +DoNotEcho;log_flags stringtables +DoNotEcho;log_flags HLTVBroadcast +DoNotEcho;log_flags HLTVServer +DoNotEcho;log_flags VR +DoNotEcho;log_flags InputService +DoNotEcho;log_flags NetworkClientService +DoNotEcho;log_flags NetworkP2PService +DoNotEcho;log_flags NetworkServerService +DoNotEcho;log_flags NetworkService +DoNotEcho;log_flags RenderService +DoNotEcho;log_flags ScreenShot +DoNotEcho;log_flags SplitScreen +DoNotEcho;log_flags VProf +DoNotEcho;log_flags BitBufError +DoNotEcho;log_flags Client +DoNotEcho;log_flags CommandLine +DoNotEcho;log_flags EngineServiceManager +DoNotEcho;log_flags GameEventSystem +DoNotEcho;log_flags HostStateManager +DoNotEcho;log_flags Filesystem +DoNotEcho;log_flags InputSystem +DoNotEcho;log_flags IME +DoNotEcho;log_flags LocalizationSystem +DoNotEcho;log_flags D3D +DoNotEcho;log_flags RenderSystem +DoNotEcho;log_flags ResourceSystem +DoNotEcho;log_flags SchemaSystem +DoNotEcho;log_flags TypeManager +DoNotEcho;log_flags Vfx +DoNotEcho;log_flags MaterialSystem +DoNotEcho;log_flags PostProcessing +DoNotEcho;log_flags modellib +DoNotEcho;log_flags Physics +DoNotEcho;log_flags MeshSystem +DoNotEcho;log_flags WorldRenderer +DoNotEcho;log_flags Pulse +DoNotEcho;log_flags PulseV8 +DoNotEcho;log_flags Networking +DoNotEcho;log_flags NetworkingReliable +DoNotEcho;log_flags NetSteamConn +DoNotEcho;log_flags SteamNetSockets +DoNotEcho;log_flags AnimationGraph +DoNotEcho;log_flags BoneSetup +DoNotEcho;log_flags AnimationSystemIK +DoNotEcho;log_flags AnimationSystem +DoNotEcho;log_flags AnimResource +DoNotEcho;log_flags Interpolation +DoNotEcho;log_flags DualHull +DoNotEcho;log_flags SoundSystemLowLevel +DoNotEcho;log_flags SoundOperatorSystem +DoNotEcho;log_flags SoundSystem +DoNotEcho;log_flags SndOperators +DoNotEcho;log_flags SteamAudio +DoNotEcho;log_flags LIGHTBINNER +DoNotEcho;log_flags SceneSystem +DoNotEcho;log_flags CharacterDecalSystem +DoNotEcho;log_flags ToneMapping +DoNotEcho;log_flags VolumetricFog +DoNotEcho;log_flags ParticlesLib +DoNotEcho;log_flags Particles +DoNotEcho;log_flags PanoramaVideoPlayer +DoNotEcho;log_flags PanoramaContent +DoNotEcho;log_flags VNotify +DoNotEcho;log_flags Panorama +DoNotEcho;log_flags PanoramaScript +DoNotEcho;log_flags Workshop +DoNotEcho;log_flags SoundOpGameSystem +DoNotEcho;log_flags VScriptScripts +DoNotEcho;log_flags SaveRestore +DoNotEcho;log_flags SaveRestoreSyncIO +DoNotEcho;log_flags Elapsed +DoNotEcho;log_flags SaveRestoreIO +DoNotEcho;log_flags SaveRestoreIOFiltered +DoNotEcho;log_flags ClientMessages +DoNotEcho;log_flags GlobalState +DoNotEcho;log_flags WebApi +DoNotEcho;log_flags HltvDirector +DoNotEcho;log_flags CommandQueue +DoNotEcho;log_flags CommandQueueEvents +DoNotEcho;log_flags CommandQueueSAMPLES +DoNotEcho;log_flags ScenePrint +DoNotEcho;log_flags EmitSound +DoNotEcho;log_flags SndEmitterSystem +DoNotEcho;log_flags Wearable +DoNotEcho;log_flags SteamUnifiedMessages +DoNotEcho;log_flags GCClient +DoNotEcho;log_flags SOCache +DoNotEcho;log_flags NavMesh +DoNotEcho;log_flags RESPONSE_RULES +DoNotEcho;log_flags BuildCubemaps +DoNotEcho;log_flags EntityDump +DoNotEcho;log_flags UserMessages +DoNotEcho;log_flags Decals +DoNotEcho;log_flags Prediction +DoNotEcho;log_flags SubtitlesandCaptions +DoNotEcho;log_flags ConfigImport +DoNotEcho;log_flags CsIconGenerator +DoNotEcho;log_flags UIMapPreviews +DoNotEcho;log_flags CSGOgameinstructor +DoNotEcho;log_flags Matchmaking +DoNotEcho;log_flags RenderPipelineCsgo +DoNotEcho;log_flags RenderPipelineCsgoPostHud +DoNotEcho;log_flags Host +DoNotEcho;log_flags RESPONSEDOC_LIB +DoNotEcho;log_flags SceneFileCache +DoNotEcho;log_flags CSGO_MainMenu +DoNotEcho;cl_track_render_eye_angles 1;clear; >"%cs2path%\cfg\viewangles.cfg"
    """.strip()

    with open(os.path.join(cs2path, 'cfg', 'viewangles.cfg'), 'w') as file:
        file.write(viewangles_commands)

def launch(steampath, cs2path):
    config(cs2path)
    os.system('cls')
    
    command = f'"{steampath}\\steam.exe" -applaunch 730 -condebug -conclearlog +exec viewangles'
    subprocess.Popen(command, shell=True)

    time.sleep(5)

def tail_f(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

def angles(cs2path, host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print('Connected!')
    console_log_path = os.path.join(cs2path, "console.log")
    if not os.path.exists(console_log_path):
        while not os.path.exists(console_log_path):
            time.sleep(1)

    lasttime = 0
    interval = 1

    for line in tail_f(console_log_path):
        current = time.time()
        if "Render eye angles:" in line and current - lasttime >= interval:
            angles = line.split("Render eye angles:")[-1].strip()
            formatted_angles = ', '.join([f"{float(angle):.2f}" for angle in angles.split(", ")])
            message = formatted_angles + '                 \r'
            client.sendall(message.encode('utf-8'))
            lasttime = current

steampath = getpath(r"SOFTWARE\WOW6432Node\Valve\Steam", "InstallPath")
cs2path = getpath(r"SOFTWARE\WOW6432Node\Valve\cs2", "installpath") + r"\game\csgo"

host = input('host: ')
port = 1337
launch(steampath, cs2path)
angles(cs2path, host, port)