#%%
from pypdf import PdfReader
from backend.constants import DATA_PATH

path = DATA_PATH / "Dwarf_Hotot.pdf"
reader = PdfReader(path)


#%%