import ROOT

# run by typing: source /proj/common/sw/root/6.06.08/bin/thisroot.sh
# wavelength, incident angle, % trans/refl
transmission_data = [
[385, 0.0, 0.1661022624],
[385, 5.0, 0.2781432957],
[385, 10.0, 0.3229797539],
[385, 15.0, 0.1712141695],
[385, 20.0, 0.1890538861],
[385, 25.0, 0.0823944457],
[385, 30.0, 0.1065793646],
[385, 35.0, 0.0966665245],
[385, 40.0, 0.1265006139],
[385, 45.0, 0.1124464289],
[385, 50.0, 0.1725080839],
[385, 55.0, 0.2591059941],
[385, 60.0, 0.3271231595],
[385, 65.0, 0.4200583444],
[385, 70.0, 0.7343549106],
[405, 0.0, 0.03331896718],
[405, 5.0, 0.03897562812],
[405, 10.0, 0.04605837747],
[405, 15.0, 0.04780363843],
[405, 20.0, 0.0403511932],
[405, 25.0, 0.03016591943],
[405, 30.0, 0.04195651239],
[405, 35.0, 0.04383845055],
[405, 40.0, 0.07526152332],
[405, 45.0, 0.1047139056],
[405, 50.0, 0.1695660018],
[405, 55.0, 0.512952533],
[405, 60.0, 0.6160127367],
[405, 65.0, 1.992120785],
[405, 70.0, 5.224262006],
[450, 0.0, 0.9148144423],
[450, 5.0, 0.8725238668],
[450, 10.0, 0.8535426163],
[450, 15.0, 0.9306452534],
[450, 20.0, 1.2095242981],
[450, 25.0, 1.6414915647],
[450, 30.0, 2.6296615394],
[450, 35.0, 3.7005044242],
[450, 40.0, 6.3895756516],
[450, 45.0, 13.4876844018],
[450, 50.0, 28.538429972],
[450, 55.0, 39.958517332],
[450, 60.0, 49.0745251077],
[450, 65.0, 55.7218263337],
[450, 70.0, 60.4809830023],
[505, 0.0, 75.1963470333],
[505, 5.0, 68.5437007583],
[505, 10.0, 68.6407427757],
[505, 15.0, 76.3041537728],
[505, 20.0, 76.7000592454],
[505, 25.0, 79.4621338899],
[505, 30.0, 83.8542439913],
[505, 35.0, 85.1699597394],
[505, 40.0, 89.2963897182],
[505, 45.0, 88.0811843699],
[505, 50.0, 88.2819296561],
[505, 55.0, 88.0194098353],
[505, 60.0, 86.8441114363],
[505, 65.0, 84.9165936628],
[505, 70.0, 79.8116487312],
# reverse here...
[525, 0.0, 89.1814912505],
[525, 5.0, 88.2877318061],
[525, 10.0, 88.2883701483],
[525, 15.0, 88.6238234312],
[525, 20.0, 92.9273662605],
[525, 25.0, 88.849181328],
[525, 30.0, 89.4064831996],
[525, 35.0, 89.6232134836],
[525, 40.0, 88.4677565799],
[525, 45.0, 88.0825182311],
[525, 50.0, 88.1121898268],
[525, 55.0, 88.15690228],
[525, 60.0, 87.2311073956],
[525, 65.0, 85.7851836134],
[525, 70.0, 80.030954668],
[555, 0.0, 99.7673537912],
[555, 5.0, 99.7899918931],
[555, 10.0, 98.9009154373],
[555, 15.0, 96.9323190654],
[555, 20.0, 94.0782664015],
[555, 25.0, 93.6646169735],
[555, 30.0, 94.2356268147],
[555, 35.0, 94.5057794572],
[555, 40.0, 94.3636978702],
[555, 45.0, 93.5834364154],
[555, 50.0, 92.4894341402],
[555, 55.0, 90.0348295954],
[555, 60.0, 88.5033278771],
[555, 65.0, 83.0354031109],
[555, 70.0, 78.4894175197],
[590, 0.0, 91.5105517056],
[590, 5.0, 90.3867561541],
[590, 10.0, 90.6851366376],
[590, 15.0, 90.794423485],
[590, 20.0, 88.8749232543],
[590, 25.0, 90.4164431848],
[590, 30.0, 88.2213759744],
[590, 35.0, 87.7806507238],
[590, 40.0, 93.0335218665],
[590, 45.0, 92.8907946546],
[590, 50.0, 92.4838672387],
[590, 55.0, 88.6855182641],
[590, 60.0, 83.5320708434],
[590, 65.0, 78.4018755691],
[590, 70.0, 67.033193104],
]

reflection_data = [
#[385, 0.0, -0.0047586307],
#[385, 5.0, 0.0639699731],
#[385, 10.0, -0.0150487485],
[385, 15.0, 24.7228033055],
[385, 20.0, 48.1608056469],
[385, 25.0, 74.9648071216],
[385, 30.0, 89.1680132701],
[385, 35.0, 90.1186694421],
[385, 40.0, 93.2165840513],
[385, 45.0, 96.4574034509],
[385, 50.0, 97.7328846349],
[385, 55.0, 97.5158785359],
[385, 60.0, 95.4261697024],
[385, 65.0, 92.8088902731],
[385, 70.0, 86.8875780757],
#[405, 0.0, 0.006996886066],
#[405, 5.0, -0.003454074449],
#[405, 10.0, 0.01062474268],
[405, 15.0, 30.17660141],
[405, 20.0, 71.3677228],
[405, 25.0, 86.30467723],
[405, 30.0, 95.30069886],
[405, 35.0, 100.1656301],
[405, 40.0, 93.21657486],
[405, 45.0, 97.60564812],
[405, 50.0, 100.3316519],
[405, 55.0, 99.6925156],
[405, 60.0, 87.54272385],
[405, 65.0, 96.68762371],
[405, 70.0, 91.72794474],
#[450, 0.0, 0.0069268687],
#[450, 5.0, 0.0060668517],
#[450, 10.0, 0.0068190978],
[450, 15.0, 49.2120381949],
[450, 20.0, 75.3859982815],
[450, 25.0, 90.702144858],
[450, 30.0, 94.7125532854],
[450, 35.0, 94.3947794088],
[450, 40.0, 88.7772924539],
[450, 45.0, 87.468723402],
[450, 50.0, 72.6646499223],
[450, 55.0, 60.8359650171],
[450, 60.0, 50.850088325],
[450, 65.0, 39.6964587563],
[450, 70.0, 24.3866885717],
#[505, 0.0, 0.1048884286],
#[505, 5.0, 0.0954863942],
#[505, 10.0, 0.0950995358],
[505, 15.0, 17.2148651494],
[505, 20.0, 19.8569949445],
[505, 25.0, 19.0235396277],
[505, 30.0, 15.5272120553],
[505, 35.0, 12.4472005159],
[505, 40.0, 10.0756384746],
[505, 45.0, 9.1520366306],
[505, 50.0, 9.1232655377],
[505, 55.0, 9.6273783139],
[505, 60.0, 11.5777481495],
[505, 65.0, 14.0407561947],
[505, 70.0, 16.8939727671],
# reverse here...
#[525, 0.0, 0.0059734941],
#[525, 5.0, 0.0114716588],
#[525, 10.0, 0.013499152],
[525, 15.0, 1.3088549838],
[525, 20.0, 6.5571581444],
[525, 25.0, 7.2843255179],
[525, 30.0, 7.5421605025],
[525, 35.0, 7.7376638041],
[525, 40.0, 8.0052576036],
[525, 45.0, 8.3447959043],
[525, 50.0, 8.8282703537],
[525, 55.0, 9.5597308274],
[525, 60.0, 10.1171225618],
[525, 65.0, 11.7977008534],
[525, 70.0, 14.0171765016],
#[555, 0.0, -0.0114023633],
#[555, 5.0, 0.0048673041],
#[555, 10.0, 0.0041044197],
[555, 15.0, 1.7585300943],
[555, 20.0, 3.8949187137],
[555, 25.0, 4.8540163702],
[555, 30.0, 5.2116676832],
[555, 35.0, 5.5073532524],
[555, 40.0, 5.58343816],
[555, 45.0, 5.8783599227],
[555, 50.0, 6.3804411879],
[555, 55.0, 7.9068821817],
[555, 60.0, 8.7223092869],
[555, 65.0, 9.0503907612],
[555, 70.0, 4.9662651436],
#[590, 0.0, -0.0040518125],
#[590, 5.0, 0.0007528845],
#[590, 10.0, -0.0018721027],
[590, 15.0, 2.0719838891],
[590, 20.0, 3.6253165076],
[590, 25.0, 4.918945339],
[590, 30.0, 4.6444271162],
[590, 35.0, 4.9356233645],
[590, 40.0, 5.4665827259],
[590, 45.0, 5.9528114775],
[590, 50.0, 7.1487447702],
[590, 55.0, 7.5440064319],
[590, 60.0, 8.5496935002],
[590, 65.0, 11.0662898772],
[590, 70.0, 12.883149515],
]

sum_data = [
#[385, 0.0, 0.1613436317],
#[385, 5.0, 0.3421132688],
#[385, 10.0, 0.3079310054],
[385, 15.0, 24.894017475],
[385, 20.0, 48.349859533],
[385, 25.0, 75.0472015673],
[385, 30.0, 89.2745926347],
[385, 35.0, 90.2153359665],
[385, 40.0, 93.3430846651],
[385, 45.0, 96.5698498798],
[385, 50.0, 97.9053927188],
[385, 55.0, 97.7749845301],
[385, 60.0, 95.7532928619],
[385, 65.0, 93.2289486175],
[385, 70.0, 87.6219329863],
#[405, 0.0, 0.04031585325],
#[405, 5.0, 0.03552155367],
#[405, 10.0, 0.05668312015],
[405, 15.0, 30.22440505],
[405, 20.0, 71.40807399],
[405, 25.0, 86.33484315],
[405, 30.0, 95.34265538],
[405, 35.0, 100.2094686],
[405, 40.0, 93.29183638],
[405, 45.0, 97.71036203],
[405, 50.0, 100.5012179],
[405, 55.0, 100.2054681],
[405, 60.0, 88.15873659],
[405, 65.0, 98.67974449],
[405, 70.0, 96.95220674],
#[450, 0.0, 0.921741311],
#[450, 5.0, 0.8785907185],
#[450, 10.0, 0.8603617141],
[450, 15.0, 50.1426834484],
[450, 20.0, 76.5955225796],
[450, 25.0, 92.3436364227],
[450, 30.0, 97.3422148248],
[450, 35.0, 98.095283833],
[450, 40.0, 95.1668681055],
[450, 45.0, 100.9564078037],
[450, 50.0, 101.2030798944],
[450, 55.0, 100.7944823492],
[450, 60.0, 99.9246134327],
[450, 65.0, 95.41828509],
[450, 70.0, 84.867671574],
#[505, 0.0, 75.3012354618],
#[505, 5.0, 68.6391871525],
#[505, 10.0, 68.7358423116],
[505, 15.0, 93.5190189222],
[505, 20.0, 96.5570541898],
[505, 25.0, 98.4856735177],
[505, 30.0, 99.3814560466],
[505, 35.0, 97.6171602554],
[505, 40.0, 99.3720281928],
[505, 45.0, 97.2332210005],
[505, 50.0, 97.4051951938],
[505, 55.0, 97.6467881492],
[505, 60.0, 98.4218595858],
[505, 65.0, 98.9573498575],
[505, 70.0, 96.7056214983],
# reverse here...
#[525, 0.0, 89.1874647446],
#[525, 5.0, 88.2992034649],
#[525, 10.0, 88.3018693003],
[525, 15.0, 89.932678415],
[525, 20.0, 99.4845244049],
[525, 25.0, 96.1335068458],
[525, 30.0, 96.9486437021],
[525, 35.0, 97.3608772877],
[525, 40.0, 96.4730141835],
[525, 45.0, 96.4273141354],
[525, 50.0, 96.9404601806],
[525, 55.0, 97.7166331074],
[525, 60.0, 97.3482299574],
[525, 65.0, 97.5828844668],
[525, 70.0, 94.0481311696],
#[555, 0.0, 99.7559514279],
#[555, 5.0, 99.7948591971],
#[555, 10.0, 98.905019857],
[555, 15.0, 98.6908491598],
[555, 20.0, 97.9731851152],
[555, 25.0, 98.5186333438],
[555, 30.0, 99.4472944979],
[555, 35.0, 100.0131327096],
[555, 40.0, 99.9471360302],
[555, 45.0, 99.4617963381],
[555, 50.0, 98.8698753281],
[555, 55.0, 97.9417117771],
[555, 60.0, 97.225637164],
[555, 65.0, 92.0857938721],
[555, 70.0, 83.4556826633],
#[590, 0.0, 91.5064998931],
#[590, 5.0, 90.3875090386],
#[590, 10.0, 90.6832645349],
[590, 15.0, 92.8664073741],
[590, 20.0, 92.5002397619],
[590, 25.0, 95.3353885238],
[590, 30.0, 92.8658030906],
[590, 35.0, 92.7162740883],
[590, 40.0, 98.5001045924],
[590, 45.0, 98.8436061321],
[590, 50.0, 99.6326120089],
[590, 55.0, 96.229524696],
[590, 60.0, 92.0817643436],
[590, 65.0, 89.4681654463],
[590, 70.0, 79.916342619],
]

if __name__=='__main__':

    import sys

    n = sys.argv[1]
    if n.lower() == 'reflection':
        data = reflection_data
        xaxis = "Reflection (%)"
    elif n.lower() == 'transmission':
        data = transmission_data
        xaxis = "Transmission (%)" 
    elif n.lower() == 'sum':
        data = sum_data
        xaxis = "Sum (%)"
    else:
        print "Error, select refl, sum, or trans data."
        sys.exit(1)

    g = ROOT.TGraph2D()
    
    for i in range(len(data)):
    
        print data[i][0], data[i][1], data[i][2]
        g.SetPoint(i, data[i][1], data[i][0], data[i][2])
    
    c1 = ROOT.TCanvas("c1","c1",800,600)
    
    ROOT.gStyle.SetPalette(ROOT.kRainBow)
 
    g.GetHistogram().GetXaxis().SetTitleFont(132)
    g.GetHistogram().GetYaxis().SetTitleFont(132)
    g.GetHistogram().GetZaxis().SetTitleFont(132)
    g.GetHistogram().GetYaxis().SetTitleOffset(1.2)
 
    g.GetHistogram().GetXaxis().SetLabelFont(132)
    g.GetHistogram().GetYaxis().SetLabelFont(132)
    g.GetHistogram().GetZaxis().SetLabelFont(132)

    g.GetHistogram().GetXaxis().SetTitle("Incident Angle (#circ)")
    g.GetHistogram().GetYaxis().SetTitle("Wavelength (nm)")
    g.GetHistogram().GetZaxis().SetTitle(xaxis)
    
    g.GetHistogram().SetTitle("Various Wavelength LEDs with 480nm Long Pass Dichroic Filter")

    g.Draw("colz")
    c1.SetRightMargin(0.15)
    c1.Update()
    
    raw_input()
