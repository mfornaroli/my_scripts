# aprire file in scrittura cancella contenuto del file, dude.
f = open(r"C:\Users\Mfornaroli\Desktop\cartella temp\datalog_magnum\output_analysis.txt", mode = "rb")
print(f.readlines())
f.close()
f = open(r"C:\Users\Mfornaroli\Desktop\cartella temp\datalog_magnum\output_analysis.txt")
print(f.readlines())
f.close()
f = open(r"C:\Users\Mfornaroli\Desktop\cartella temp\datalog_magnum\output_analysis_1.txt", "a")
f.write("\n hello world!")
f.close()
