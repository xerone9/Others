import svgwrite
import win32print
import win32api
import os



dwg = svgwrite.Drawing('work.svg', size=("811px", "278px"), profile='tiny')
# svgwrite.shapes.Line(start=(1, 1), end=(811, 1),)
dwg.add(dwg.line((1, 1), (811, 1), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.line((1, 1), (1, 278), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.line((1, 278), (811, 278), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.line((811, 1), (811, 278), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('12-12-2022', insert=(650, 60.8), fill='black'))
dwg.add(dwg.text('Umer Murtaza Khawar', insert=(223, 99.28), fill='black', ))
dwg.add(dwg.text('Four Thousand Rupees Only', insert=(248, 125.2), fill='black'))
dwg.add(dwg.text('4000/-', insert=(680, 122.4), fill='black'))
dwg.add(dwg.text('12-12-2022', insert=(80.4, 86.2), font_size="10px",fill='black'))
dwg.add(dwg.text('Umer Murtaza Khawar', insert=(76.0, 99.8), font_size="10px",fill='black'))
dwg.add(dwg.text('4000/-', insert=(95, 191.6), font_size="10px",fill='black'))

dwg.save()

printer_name = win32print.GetDefaultPrinter()
win32print.OpenPrinter(printer_name)
# os.startfile("test.svg", "print")
win32api.ShellExecute(0, "print", "work.svg", None,  ".",  0)