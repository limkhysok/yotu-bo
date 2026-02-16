# Global Style Constants
STYLESHEET = """
    QMainWindow { 
        background-color: #121212; 
    }
    
    QWidget { 
        color: #E0E0E0; 
        font-family: 'Jost', system-ui, sans-serif; 
    }
    
    #navbar {
        background-color: #1E1E1E;
        border-bottom: 1px solid #4A4A4A;
        min-height: 40px;
        max-height: 40px;
    }
    
    #sidebar { 
        background-color: #121212; 
        border-right: 1px solid #4A4A4A; 
        min-width: 100px; 
        max-width: 100px; 
    }
    
    QPushButton#sidebar-item { 
        text-align: left; 
        padding: 12px 15px; 
        background: transparent; 
        color: #E0E0E0; 
        border: none; 
        font-size: 14px;
        font-weight: 500;
    }
    
    QPushButton#sidebar-item:hover { 
        background: #1E1E1E; 
        color: #D32F2F; 
    }
    
    QPushButton#sidebar-item[active="true"] { 
        background: #1E1E1E; 
        color: #D32F2F; 
        border-left: 4px solid #D32F2F;
        font-weight: 700;
    }
    
    #nav-action-btn {
        background-color: transparent;
        color: #E0E0E0;
        border: none;
        border-radius: 17px;
        padding: 0px;
        min-height: 34px;
        max-height: 34px;
        min-width: 34px;
        max-width: 34px;
    }
    
    #nav-action-btn:hover {
        background-color: #8B0000;
        border-radius: 17px;
    }

    /* Page Styles */
    QLabel#page-header {
        font-size: 28px; 
        font-weight: bold; 
        color: #D32F2F;
    }
    
    QFrame#card {
        background-color: #1E1E1E;
        border: 1px solid #4A4A4A;
        border-radius: 12px;
        padding: 20px;
    }

    QLineEdit {
        background-color: #121212;
        border: 1px solid #4A4A4A;
        border-radius: 6px;
        padding: 12px;
        color: #E0E0E0;
        font-size: 14px;
    }
    
    QLineEdit:focus {
        border-color: #D32F2F;
    }
    
    QPushButton#primary-btn {
        background-color: #D32F2F;
        color: #E0E0E0;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 800;
    }
    
    QPushButton#primary-btn:hover {
        background-color: #8B0000;
    }

    QTextEdit#console {
        background-color: #000000;
        border: 1px solid #4A4A4A;
        border-radius: 10px;
        color: #D32F2F;
        font-family: 'Consolas', monospace;
        font-size: 13px;
        padding: 15px;
    }
"""

THEME_COLORS = {
    "PRIMARY_RED": "#D32F2F",  # Aggressive highlight
    "DARK_RED": "#8B0000",  # Hover/Pressed state
    "BASE_BLACK": "#121212",  # Main background
    "SURFACE_BLACK": "#1E1E1E",  # Card/Container background
    "SILVER_TEXT": "#E0E0E0",  # Primary text
    "SILVER_BORDER": "#4A4A4A",  # Subtle borders
    "SILVER_METALLIC": "#C0C0C0",  # Highlights/Icons
}
