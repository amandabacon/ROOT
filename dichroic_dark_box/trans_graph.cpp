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
    Float_t yf5nt_stable_385[n] = {};

// 405nm
    Float_t yf5nt_stable_405[n] = {};

// 450nm
    Float_t yf5nt_stable_450[n] = {};

// 505nm
    Float_t yt5nt_stable_505[n] = {};

// 525nm
    Float_t yf5nt_stable_525[n] = {};

// 555nm
    Float_t ys5nt_stable_555[n] = {};

// 590nm
    Float_t ys5nt_stable_590[n] = {};

    c1->SetGrid();

    TGraph *trans_385 = new TGraph(n,x,yf5nt_stable_385); // light b/v
    TGraph *trans_405 = new TGraph(n,x,yf5nt_stable_405); // violet
    TGraph *trans_450 = new TGraph(n,x,yf5nt_stable_450); // blue
    TGraph *trans_505 = new TGraph(n,x,yt5nt_stable_505); // azure
    TGraph *trans_525 = new TGraph(n,x,yf5nt_stable_525); // green
    TGraph *trans_555 = new TGraph(n,x,ys5nt_stable_555); // spring
    TGraph *trans_590 = new TGraph(n,x,ys5nt_stable_590); // yellow

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

    trans_450->Draw("ALP");
    trans_385->Draw("LP");
    trans_405->Draw("LP");
    trans_505->Draw("LP");
    trans_525->Draw("LP");
    trans_555->Draw("LP");
    trans_590->Draw("LP");

    c1->Update();

    TLegend *legend = new TLegend(0.1,0.4,0.3,0.6); // L,B,R,T 
    legend->AddEntry(trans_385, "385nm"); // light b/v
    legend->AddEntry(trans_405, "405nm"); // violet
    legend->AddEntry(trans_450, "450nm"); // blue
    legend->AddEntry(trans_505, "505nm"); // azure
    legend->AddEntry(trans_525, "525nm"); // green
    legend->AddEntry(trans_555, "555nm"); // green-yellow
    legend->AddEntry(trans_590, "590nm"); // yellow
    legend->SetTextFont(132);
    legend->SetFillColor(0);
    legend->SetFillStyle(0);
    legend->Draw();
    c1->Update();
}
