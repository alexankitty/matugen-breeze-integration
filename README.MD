# Matugen Breeze Integration
Basic integation of Matugen with the Breeze theme for gtk and qt.

# Setup
Install the following `breeze breeze5 breeze-icons breeze-gtk qt6ct-kde qt5ct-kde`  
Copy the contents of the repo to `~/.config/`  
This will replace your gtk/qt configs, so make sure to back up gtk-3.0, gtk-4.0, qt5ct, and qt6ct folders in .config.

# Config
Set your Qt application style or QT_QPA_PLATFORMTHEME variable to qt6ct  
I recommend setting your icons and colors to Breeze Dark.  
In your Qt6ct/Qt5ct config, set the application style to Breeze and the color scheme to matugen.

# Note
Includes templates stolen from [InioX's matugen-themes](https://github.com/InioX/matugen-themes) repo.  
Instructions on how to use the rest of the templates are on the matugen-themes repo.  

# Fixes
The gtk-3.0 folder contains a fix for the vmware/omnissa horizon client.  
If you're unfortunate to need this and use a dark theme, you can add an import to your gtk-3.0/gtk.css. `@import 'horizon-client.css'`

