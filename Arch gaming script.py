from os import system, chdir
import readline
import time

from colorama import Fore, Back, Style
print(Fore.RED + "Which aur helper will you use?")
print(Style.RESET_ALL)

aur_helper = input("yay , paru = ")

if aur_helper == "paru":
                 system("git clone https://aur.archlinux.org/paru.git && cd paru &&  makepkg -si")
                 
if aur_helper == "yay":
                 system("git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")                
system("clear")

aur_helper = input("what is your aur helper? = ")

system("clear")

print(Fore.RED + "Which desktop environment will you use?")
print(Style.RESET_ALL)

de = input("gnome , gnome debloated , xfce4 , kde plasma , kde plasma minimal = ")

if de == "gnome":
          system("sudo pacman -S gnome xorg xorg-xinit")
          input("press enter to continue")

if de == "gnome debloated":          
          system("sudo pacman -S eog evince file-roller gnome-backgrounds gnome-characters gnome-color-manager gnome-terminal gnome-control-center gnome-disk-utility gnome-menus gnome-session gnome-settings-daemon gnome-shell gnome-shell-extensions gnome-text-editor gnome-tweaks gvfs gvfs-afc gvfs-mtp nautilus xdg-user-dirs-gtk xdg-desktop-portal xdg-desktop-portal-gnome xdg-desktop-portal-gtk xdg-user-dirs xdg-utils xorg xorg-xinit")
          input("press enter to continue")

if de == "xfce4":
          system("sudo pacman -S xfce4 xfce4-goodies xorg xorg-xinit")
          input("press enter to continue") 

if de == "kde plasma minimal":
          system("sudo pacman -S plasma-desktop konsole dolphin ark")
          input("press enter to continue") 
if de == "kde plasma": 
          system("sudo pacman -S xorg xorg-xinit plasma plasma-wayland-session kde-applications")          
          input("press enter to continue")  

system("clear")
 
print(Fore.RED + "Which Display Manager do you use?")
print(Style.RESET_ALL)

dm = input("lightdm , sddm , ly , gdm = " )

if dm == "lightdm":
    system("sudo pacman -S lightdm lightdm-gtk-greeter && sudo systemctl enable lightdm")
    
if dm == "sddm":
    system("sudo pacman -S sddm && sudo systemctl enable sddm")
    
if dm == "ly":
    system("sudo pacman -S ly && sudo systemctl enable ly")
    
if dm == "gdm":
    system("sudo pacman -S gdm && sudo systemctl enable gdm")

system("clear")
                 
kernel = input("zen kernel , lts kernel , xanmod kernel? = ")

if kernel == "zen kernel":
    system("sudo pacman -S linux-zen linux-zen-headers")
    input("press enter to continue")
    
if kernel == "lts kernel":
    system("sudo pacman -S linux-lts linux-lts-headers")
    input("press enter to continue")
    
if kernel == "xanmod kernel":    
    system("sudo pacman -S linux-xanmod linux-xanmod-headers")   
    input("press enter to continue")
    
system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
input("press enter to continue")
    
system("clear")
    
gpu = input("amd , nvidia , intel , intel-nvidia? = ")

if gpu == "amd":
    system("sudo pacman -S --needed lib32-mesa vulkan-radeon lib32-vulkan-radeon vulkan-icd-loader lib32-vulkan-icd-loader")
    input("press enter to continue")

if gpu == "nvidia":
    system("sudo pacman -S --needed nvidia-dkms nvidia-settings nvidia-utils opencl-nvidia primus_vk python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia lib32-primus_vk python-glfw vkd3d lib32-vkd3d")
    input("press enter to continue")

if gpu == "intel":
    system("sudo pacman -S --needed mesa lib32-mesa libva-intel-driver lib32-libva-intel-driver")
    input("press enter to continue")

if gpu == "intel-nvidia":
    system("sudo pacman -S --needed mesa lib32-mesa libva-intel-driver lib32-libva-intel-driver nvidia-dkms nvidia-settings nvidia-utils opencl-nvidia primus_vk python-pycuda lib32-libvdpau lib32-nvidia-utils lib32-opencl-nvidia lib32-primus_vk python-glfw vkd3d lib32-vkd3d")
    input("press enter to continue")    

system("clear")

print(Fore.RED + "if you want to install bbswitch write yes. If you dont want it write no.")
print(Style.RESET_ALL)

bbswitch = input("yes , no? = ")

if bbswitch == "yes":
    system("sudo pacman -S bbswitch-dkms")
    input("press enter to continue") 
    
if bbswitch == "no":
    input("press enter to continue")    

system("clear")

print(Fore.RED + "Do you want to undervolt ypur intel cpu?.")
print(Style.RESET_ALL)

undervolt = input("yes , no = ")

if undervolt == "yes":
    system("sudo pacman -S intel-undervolt nano && sudo nano /etc/intel-undervolt.conf && sudo systemctl enable intel-undervolt.service")

if undervolt == "no":
    input("press enter to continue")            

print(Fore.RED + "Do you want optimus-manager?(just intel-nvidia and amd-nvidia users)")
print(Style.RESET_ALL)

optimus = input("yes , no = " )

if optimus == "yes":
     system(f"{aur_helper} -S optimus-manager && sudo cp /usr/share/optimus-manager.conf /etc/optimus-manager/optimus-manager.conf && sudo nano /etc/optimus-manager/optimus-manager.conf")

if optimus == "no":
     input("press enter to continue")     

system("clear")

print(Fore.RED + "Now the necessary packages for the games will be installed.")
print(Style.RESET_ALL)
input("press enter to continue")

system(f"{aur_helper} -S --needed lutris vkd3d wine-mono lib32-vkd3d wine-staging winetricks bottles protontricks-git protonup-qt wine-lol dxvk-bin steam steam-native-runtime")
input("press enter to continue")
system("sudo pacman -S --needed lib32-libldap giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo libxcomposite lib32-libxcomposite libxinerama lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader gamemode innoextract lib32-gamemode lib32-vkd3d vkd3d")

system("clear")

print(Fore.RED + "when winecfg is opened, go to libraries and add d3dcompiler47, d3d10 and d3d11. d3d11 and d3d10 is need to be native, d3dcompiler is need to be default.")
print(Style.RESET_ALL)

system("winecfg")
