import tkinter
import tkintermapview
import geocoder

# Replace 'YOUR_GOOGLE_MAPS_API_KEY' with your actual API key
API_KEY= 'ethanricks03'

ADDRESSES: list[str] = ["1850 Chadwick Dr, Jackson, MS", "1134 Winter St, Jackson, MS", "5429 Robinson Rd, Jackson, MS" ]



def mapping_with_coordinates(lat : float, lon: float):
    # create tkinter window
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{800}x{600}")
    root_tk.title("map_view_example.py")

    # create map widget
    map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # set current widget position and zoom
    map_widget.set_position(lat , lon)  # Paris, France
    map_widget.set_zoom(15)

    root_tk.mainloop()

def mapping_with_address(add: str):
    # create tkinter window
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{800}x{600}")
    root_tk.title("map_view_example.py")

    # create map widget
    map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    for address in ADDRESSES:
        map_widget.set_address(address, marker=True)

    map_widget.set_address(add)

    # set current widget position and zoom
    map_widget.set_zoom(13)
    root_tk.mainloop()
    

def main():
    mapping_with_address("1400 J.R. Lynch St, Jackson, MS")
    pass


if __name__ == "__main__":
    main()