"""
Customization Module for UI styling and settings management
"""

import json
import os
import tkinter as tk
from pathlib import Path


SETTINGS_FILE = "tts_settings.json"


def get_default_settings():
    """
    Get default settings for the application
    
    Returns:
        dict: Default settings
    """
    return {
        "font_family": "Arial",
        "font_size": 14,
        "word_spacing": 1,
        "letter_spacing": 0,
        "bg_color": "#ffffff",
        "fg_color": "#000000",
        "highlight_color": "#ffe599",
        "highlight_mode": "word"
    }


def load_settings():
    """
    Load settings from file or return defaults
    
    Returns:
        dict: User settings or defaults
    """
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r') as f:
                settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                defaults = get_default_settings()
                defaults.update(settings)
                return defaults
    except Exception as e:
        print(f"Error loading settings: {e}")
    
    return get_default_settings()


def save_settings(settings):
    """
    Save settings to file
    
    Args:
        settings (dict): Settings dictionary to save
    """
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f, indent=4)
        print("Settings saved successfully")
    except Exception as e:
        print(f"Error saving settings: {e}")


def apply_custom_style(text_widget, settings, live=False):
    """
    Apply custom styling to the text widget based on settings
    
    Args:
        text_widget: tkinter Text widget to style
        settings (dict): Settings dictionary containing font, color, and spacing options
        live (bool): Whether to apply live updates
    """
    try:
        font_family = settings.get("font_family", "Arial")
        font_size = settings.get("font_size", 14)
        bg_color = settings.get("bg_color", "#ffffff")
        fg_color = settings.get("fg_color", "#000000")
        word_spacing = settings.get("word_spacing", 1)
        letter_spacing = settings.get("letter_spacing", 0)
        
        # Configure basic font and colors
        text_widget.config(
            font=(font_family, font_size),
            bg=bg_color,
            fg=fg_color,
            spacing1=word_spacing,
            spacing2=word_spacing,
            spacing3=word_spacing
        )
        
        # Create tag for letter spacing (note: tkinter Text has limited letter spacing support)
        # We'll use a custom font with overstrike as workaround for visual spacing
        text_widget.tag_configure(
            "custom",
            font=(font_family, font_size),
            foreground=fg_color,
            background=bg_color
        )
        
    except Exception as e:
        print(f"Error applying custom style: {e}")


def reset_settings():
    """
    Reset settings to defaults and save
    """
    defaults = get_default_settings()
    save_settings(defaults)
    return defaults


def update_setting(key, value):
    """
    Update a single setting and save
    
    Args:
        key (str): Setting key
        value: Setting value
    """
    settings = load_settings()
    settings[key] = value
    save_settings(settings)


def get_setting(key, default=None):
    """
    Get a single setting value
    
    Args:
        key (str): Setting key
        default: Default value if key not found
    
    Returns:
        Setting value or default
    """
    settings = load_settings()
    return settings.get(key, default)
