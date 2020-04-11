print ("let's practice everything.")
print ("you\'d need to know \'bout escapes with \\ that do")
print ('\n newlines and \t tabs.')

peom = """
\t the lovely world 
with logic so firmly planted
cannot discern\n the nedds of love
nor comprehend passion from intuition
nd requires n explanantion
\n\t\t where there is none."""

print ('...................')

print (peom)
print ("...........")

five= 10-2+3-6+4-4
print (f"this should be five:{five}")

def secret_formula(started):
    jelly_beans= started*500
    jars =jelly_beans /1000
    crtes = jars/ 100
    return jelly_beans,jars, crtes

start_point = 10000
beans, jars,crtes =secret_formula(start_point)

print("with a starting point of :{}".format(start_point))

print(f" we'd have {beans} beans, {jars} jar, and {crtes} crates.")

start_point = start_point /10
print ("we can also do that this way:")
formula =secret_formula(start_point)

print ("WE'd have{} beans, {}jars, and {} crates.".format(*formula))

