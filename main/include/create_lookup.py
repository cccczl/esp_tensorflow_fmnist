
with open("normalisation_lookup.h", "a") as f:
	f.write("static const __flash uint8_t lookup[256] =")
	f.write("{\n")
	for i in range(0, 255, 8):
		f.write("%f ,\t"%(i/255.0))
		f.write("%f ,\t"%((i+1)/255.0))
		f.write("%f ,\t"%((i+2)/255.0))
		f.write("%f ,\t"%((i+3)/255.0))
		f.write("%f ,\t"%((i+4)/255.0))
		f.write("%f ,\t"%((i+5)/255.0))
		f.write("%f ,\t"%((i+6)/255.0))
		f.write("%f ,\t"%((i+7)/255.0))
		f.write("\n")
	f.write("}\n")