####################################/
#
# 'BASIC FUNCTIONALITY' RooFit tutorial macro #110
# 
# Examples on normalization of p.d.f.s,
# integration of p.d.fs, construction
# of cumulative distribution functions from p.d.f.s
# in one dimension
#
# 07/2008 - Wouter Verkerke 
#
####################################/

from ROOT import * 


def rf110_normintegration():
  # S e t u p   m o d e l 
  # ---------------------

  # Create observables x,y
  x = RooRealVar("x","x",-10,10) 

  # Create p.d.f. gaussx(x,-2,3) 
  gx = RooGaussian("gx","gx",x,RooFit.RooConst(-2),RooFit.RooConst(3)) 


  # R e t r i e v e   r a w  &   n o r m a l i z e d   v a l u e s   o f   R o o F i t   p . d . f . s
  # --------------------------------------------------------------------------------------------------

  # Return 'raw' unnormalized value of gx
  print "gx = ", gx.getVal()
  
  # Return value of gx normalized over x in range [-10,10]
  nset = RooArgSet(x) 
  print "gx_Norm[x] = ", gx.getVal(nset) 

  # Create object representing integral over gx
  # which is used to calculate  gx_Norm[x] == gx / gx_Int[x]
  igx = gx.createIntegral(RooArgSet(x)) 
  print "gx_Int[x] = ", igx.getVal() 


  # I n t e g r a t e   n o r m a l i z e d   p d f   o v e r   s u b r a n g e
  # ----------------------------------------------------------------------------

  # Define a range named "signal" in x from -5,5
  x.setRange("signal",-5,5) 
  
  # Create an integral of gx_Norm[x] over x in range "signal"
  # This is the fraction of of p.d.f. gx_Norm[x] which is in the
  # range named "signal"
  igx_sig = gx.createIntegral(RooArgSet(x),RooFit.NormSet(RooArgSet(x)),RooFit.Range("signal")) 
  print "gx_Int[x|signal]_Norm[x] = ", igx_sig.getVal()



  # C o n s t r u c t   c u m u l a t i v e   d i s t r i b u t i o n   f u n c t i o n   f r o m   p d f
  # -----------------------------------------------------------------------------------------------------

  # Create the cumulative distribution function of gx
  # i.e. calculate Int[-10,x] gx(x') dx'
  gx_cdf = gx.createCdf(RooArgSet(x)) 
  
  # Plot cdf of gx versus x
  frame = x.frame(RooFit.Title("c.d.f of Gaussian p.d.f")) 
  gx_cdf.plotOn(frame) 



  # Draw plot on canvas
  c = TCanvas("rf110_normintegration","rf110_normintegration",600,600) 
  gPad.SetLeftMargin(0.15) ; frame.GetYaxis().SetTitleOffset(1.6) 
  frame.Draw() 

  c.SaveAs("rf110_normintegration.png")

if __name__ == "__main__":
  rf110_normintegration()
