#!/usr/bin/env bash
sed -i "s|color_scheme_path=/|color_scheme_path=//|" "$HOME/.config/qt6ct/qt6ct.conf"
sed -i "s|color_scheme_path=/|color_scheme_path=//|" "$HOME/.config/qt5ct/qt5ct.conf"
sleep 5
sed -i "s|color_scheme_path=//|color_scheme_path=/|" "$HOME/.config/qt6ct/qt6ct.conf"
sed -i "s|color_scheme_path=//|color_scheme_path=/|" "$HOME/.config/qt5ct/qt5ct.conf"
