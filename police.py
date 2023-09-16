#coding:utf-8
#################################################################################################################
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################################################
# Utility to detect Victoria Police officers within bluetooth signal range via their body worn camera.
#################################################################################################################
'''
                                                                                                         
 *#####:         .##:*##                   @@@@@: @@@@@@=#@@@@@@#-@@@@@@  @@@@@:@@@@@@@= @@@@@@ -@@@@@   
 #######-        .##:###                   @@@@@- @@@@@@=#@@@@@@#-@@@@@@ .@@@@@:@@@@@@@= @@@@@@ -@@@@@   
 ###::###  -==:  .##:-=-   ===     ===     @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###  ### ###### .##:###  #####- .#####:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@=  @@  
 #######*-##. ##:.##:### *## ### ##+ :##   @%  %@ @@@@%     @@   -@@@@.  @@        @@   %@    @#-@@@@@   
 ######* +##  ##*.##:### ###     #######.  @%  %@ @@@@*     @@   -@@@@   @@        @@   %@    @#-@@@@@.  
 ###     =##  ##*.##:### ### :** ##+  .:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###      ###### .##:### -#####* =##*##*   @@--@# @@----.   @@   -@*---- *@----    @@   =@=--=@=-@-  @@  
 *##      .####. .##.*##  -###+   -###+    @@@@@: @@@@@@+   @@   -@@@@@@  @@@@@:   @@    @@@@@@ -@-  @@  
                                           =====. ======:   ==   .======  =====    =-    ====== .=.  ==  

"If He Was Going To Commit A Crime, Would He Have Invited The Number One Cop In Town? Now, Where Did I Put My Gun?
Oh Yeah, I Set It Down When I Got A Piece Of Cake!" - Clancy Wiggum 
'''
#################################################################################################################
# Open Sauce Software, tasty and free!
#################################################################################################################
import simplepyble, time, threading, logging, os, sys
from datetime import datetime
#################################################################################################################
current_dateTime = datetime.now()
#################################################################################################################
def logo():
    print(
            '''
#################################################################################################################
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################################################
# Utility to detect Police officers within bluetooth signal range via their body worn camera.
#################################################################################################################

                                                                                                         
 *#####:         .##:*##                   @@@@@: @@@@@@=#@@@@@@#-@@@@@@  @@@@@:@@@@@@@= @@@@@@ -@@@@@   
 #######-        .##:###                   @@@@@- @@@@@@=#@@@@@@#-@@@@@@ .@@@@@:@@@@@@@= @@@@@@ -@@@@@   
 ###::###  -==:  .##:-=-   ===     ===     @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###  ### ###### .##:###  #####- .#####:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@=  @@  
 #######*-##. ##:.##:### *## ### ##+ :##   @%  %@ @@@@%     @@   -@@@@.  @@        @@   %@    @#-@@@@@   
 ######* +##  ##*.##:### ###     #######.  @%  %@ @@@@*     @@   -@@@@   @@        @@   %@    @#-@@@@@.  
 ###     =##  ##*.##:### ### :** ##+  .:   @%  %@ @@        @@   -@=     @@        @@   %@    @#-@-  @@  
 ###      ###### .##:### -#####* =##*##*   @@--@# @@----.   @@   -@*---- *@----    @@   =@=--=@=-@-  @@  
 *##      .####. .##.*##  -###+   -###+    @@@@@: @@@@@@+   @@   -@@@@@@  @@@@@:   @@    @@@@@@ -@-  @@  
                                           =====. ======:   ==   .======  =====    =-    ====== .=.  ==  

"If He Was Going To Commit A Crime, Would He Have Invited The Number One Cop In Town? Now, Where Did I Put My Gun?
Oh Yeah, I Set It Down When I Got A Piece Of Cake!" - Clancy Wiggum

#################################################################################################################
# Open Sauce Software, tasty and free!
#################################################################################################################
                                            '''
        )
police_detected = 0
#if __name__ == "__main__":
def GetBluetoothMacList():
    global count, police_detected
    adapters = simplepyble.Adapter.get_adapters()
    if len(adapters) == 0:
        print(" >>>> No Adapters Found...")
    # Query the user to pick an adapter
    #print("Please select an adapter:")
    #for i, adapter in enumerate(adapters):
    #    print(f"{i}: {adapter.identifier()} [{adapter.address()}]")
    choice = int(0)
    adapter = adapters[choice]
    print(f" >>>> Bluetooth adapter: {adapter.identifier()} [{adapter.address()}]")
    adapter.set_callback_on_scan_start(lambda: print(" >>>> Scan started.", datetime.now()))
    adapter.set_callback_on_scan_stop(lambda: print(" >>>> Scan complete.", datetime.now()))
    adapter.set_callback_on_scan_found(lambda peripheral: print(f" > Found {peripheral.identifier()} [{peripheral.address()}]"))
    # Scan for 5 seconds
    adapter.scan_for(4500)
    peripherals = adapter.scan_get_results()
    count = count + 1
    print(" >>>> Scan Count:", count)
    #addr = "69:58"
    for peripheral in peripherals:
        #print(peripheral.address())
        #detectionslog = open("detections.log", "a")
        #print(peripheral.address(), current_dateTime, file=detectionslog)
        #detectionslog.close()
        if "00:25:DF" in peripheral.address(): # magic numbers
            # https://www.youtube.com/watch?v=6GyJZoep6rc
            # Debian GNU Linux 
            # os.system("mpv POLICE.mp4")
            # Raspberry Pi
            # os.system("omxplayer POLICE.mp4")
            police_detected = police_detected + 1
            print(" >>>>>>>>>> POLICE DETECTED:", police_detected, datetime.now())
            detectionslog = open("detections.log", "a")
            print(" >>>>>>>>>> POLICE DETECTED:", police_detected, datetime.now(), file=detectionslog)
            detectionslog.close()

            if police_detected >= 5:
                print(" >>>>>>>>>> POLICE OFFICERS DETECTED - POSSIBLE POLICE RAID IMMINENT")
                detectionslog = open("detections.log", "a")
                print(" >>>>>>>>>> POLICE OFFICERS DETECTED - POSSIBLE POLICE RAID IMMINENT ", datetime.now(), file=detectionslog)
                detectionslog.close()
            
        else:
            time.sleep(0.05125)
            print(" > No Police Detected ", datetime.now())
            #detectionslog = open("detections.log", "a")
            #print("No Police Detected ", current_dateTime, file=detectionslog)
            #detectionslog.close()
                    
def detect():
    global count, police_detected
    while True:
        try:
            logo()
            GetBluetoothMacList()
            time.sleep(2)
        except:
            pass

if __name__ == "__main__":
    count = 0
    x = threading.Thread(target=detect)
    x.start()
    # x.join()
