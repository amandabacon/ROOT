#include <iostream>
#include <TGraph.h>
#include <TCanvas.h>
#include <TLegend.h>
using namespace std;

int trans_graph(){
    TCanvas *c1 = new TCanvas("c1","Simple Graph",700,500); // width & height

    const Int_t n = 15; // remove 75 and 80 degrees due to grazing

    Float_t x[n] = {0.0,5.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0};

// 385nm
    Float_t yf5nt_stable_385[n] = {0.1661022624,0.2781432957,0.3229797539,0.1712141695,0.1890538861,0.0823944457,0.1065793646,0.0966665245,0.1265006139,0.1124464289,0.1725080839,0.2591059941,0.3271231595,0.4200583444,0.7343549106}; // Oct 25-T

// 405nm
    Float_t yf5nt_stable_405[n] = {0.03331896718,0.03897562812,0.04605837747,0.04780363843,0.0403511932,0.03016591943,0.04195651239,0.04383845055,0.07526152332,0.1047139056,0.1695660018,0.512952533,0.6160127367,1.992120785,5.224262006}; // Oct 10-T

// 450nm
    Float_t yf5nt_stable_450[n] = {0.9148144423,0.8725238668,0.8535426163,0.9306452534,1.2095242981,1.6414915647,2.6296615394,3.7005044242,6.3895756516,13.4876844018,28.538429972,39.958517332,49.0745251077,55.7218263337,60.4809830023}; // Sept 06-T

// 505nm
    Float_t yt5nt_stable_505[n] = {75.1963470333,68.5437007583,68.6407427757,76.3041537728,76.7000592454,79.4621338899,83.8542439913,85.1699597394,89.2963897182,88.0811843699,88.2819296561,88.0194098353,86.8441114363,84.9165936628,79.8116487312}; // Sept 11/12-T

// 525nm
    Float_t yf5nt_stable_525[n] = {89.1814912505,88.2877318061,88.2883701483,88.6238234312,92.9273662605,88.849181328,89.4064831996,89.6232134836,88.4677565799,88.0825182311,88.1121898268,88.15690228,87.2311073956,85.7851836134,80.030954668}; // Sept 12-T

// 555nm
    Float_t ys5nt_stable_555[n] = {99.7673537912,99.7899918931,98.9009154373,96.9323190654,94.0782664015,93.6646169735,94.2356268147,94.5057794572,94.3636978702,93.5834364154,92.4894341402,90.0348295954,88.5033278771,83.0354031109,78.4894175197}; // Sept 05-T

// 590nm
    Float_t ys5nt_stable_590[n] = {91.5105517056,90.3867561541,90.6851366376,90.794423485,88.8749232543,90.4164431848,88.2213759744,87.7806507238,93.0335218665,92.8907946546,92.4838672387,88.6855182641,83.5320708434,78.4018755691,67.033193104}; // Sept 20-T

// 610nm


    c1->SetGrid();

    TGraph *trans_385 = new TGraph(n,x,yf5nt_stable_385); // light b/v
    TGraph *trans_405 = new TGraph(n,x,yf5nt_stable_405); // violet
    TGraph *trans_450 = new TGraph(n,x,yf5nt_stable_450); // blue
    TGraph *trans_505 = new TGraph(n,x,yt5nt_stable_505); // azure
    TGraph *trans_525 = new TGraph(n,x,yf5nt_stable_525); // green
    TGraph *trans_555 = new TGraph(n,x,ys5nt_stable_555); // spring
    TGraph *trans_590 = new TGraph(n,x,ys5nt_stable_590); // yellow
//    TGraph *trans_610 = new TGraph(n,x,ys5nt_stable_610); // orange

    trans_450->SetTitle("Various Wavelength LEDs with 480nm Long Pass Dichroic Filter");
    trans_450->GetXaxis()->SetTitle("Incident Angle");
    trans_450->GetYaxis()->SetTitle("Percent Transmittance");
    trans_450->SetMaximum(100);
    trans_450->SetMinimum(0);
    trans_450->SetMarkerColor(kBlue);
    trans_450->SetMarkerStyle(21);
    trans_450->SetFillStyle(0);
    trans_450->SetFillColor(0);
    trans_385->SetMarkerColor(kBlue-8);
    trans_385->SetMarkerStyle(21);
    trans_385->SetFillStyle(0);
    trans_385->SetFillColor(0);
    trans_405->SetMarkerColor(kViolet);
    trans_405->SetMarkerStyle(21);
    trans_405->SetFillStyle(0);
    trans_405->SetFillColor(0);
    trans_505->SetMarkerColor(kAzure+1);
    trans_505->SetMarkerStyle(21);
    trans_505->SetFillStyle(0);
    trans_505->SetFillColor(0);
    trans_525->SetMarkerColor(kGreen);
    trans_525->SetMarkerStyle(21);
    trans_525->SetFillStyle(0);
    trans_525->SetFillColor(0);
    trans_555->SetMarkerColor(kSpring+6);
    trans_555->SetMarkerStyle(21);
    trans_555->SetFillStyle(0);
    trans_555->SetFillColor(0);
    trans_590->SetMarkerColor(kYellow);
    trans_590->SetMarkerStyle(21);
    trans_590->SetFillStyle(0);
    trans_590->SetFillColor(0);
//    trans_610->SetMarkerColor(kOrange);
//    trans_610->SetMarkerStyle(21);
//    trans_610->SetFillStyle(0);
//    trans_610->SetFillColor(0);

    trans_450->Draw("ALP");
    trans_385->Draw("LP");
    trans_405->Draw("LP");
    trans_505->Draw("LP");
    trans_525->Draw("LP");
    trans_555->Draw("LP");
    trans_590->Draw("LP");
//    trans_610->Draw("LP");

    c1->Update();

    TLegend *legend = new TLegend(0.1,0.4,0.3,0.6); // L,B,R,T 
    legend->AddEntry(trans_385, "385nm October 25"); // light b/v
    legend->AddEntry(trans_405, "405nm October 10"); // violet
    legend->AddEntry(trans_450, "450nm September 6"); // blue
    legend->AddEntry(trans_505, "505nm September 12"); // azure
    legend->AddEntry(trans_525, "525nm September 12"); // green
    legend->AddEntry(trans_555, "555nm September 5"); // green-yellow
    legend->AddEntry(trans_590, "590nm September 20"); // yellow
//    legend->AddEntry(trans_610, "610nm September"); // orange
    legend->SetTextFont(132);
    legend->SetFillColor(0);
    legend->SetFillStyle(0);
    legend->Draw();
    c1->Update();
}
