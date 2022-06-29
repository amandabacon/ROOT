#include <iostream>
#include <TGraph.h>
#include <TCanvas.h>
#include <TLegend.h>
using namespace std;

int refl_graph(){
    TCanvas *c1 = new TCanvas("c1","Simple Graph",700,500); // width & height

    const Int_t n = 12; // remove 75 and 80 degrees due to grazing

    Float_t x[n] = {15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0};

// 385nm
    Float_t yf5nr_stable_385[n] = {};

// 405nm
    Float_t yf5nr_stable_405[n] = {};

// 450nm
    Float_t yf5nr_stable_450[n] = {};

// 505nm
    Float_t yt5nr_stable_505[n] = {};

// 525nm
    Float_t yf5nr_stable_525[n] = {};

// 555nm
    Float_t ys5nr_stable_555[n] = {};

// 590nm
    Float_t ys5nr_stable_590[n] = {};

    c1->SetGrid();

    TGraph *refl_385 = new TGraph(n,x,yf5nr_stable_385); // light b/v
    TGraph *refl_405 = new TGraph(n,x,yf5nr_stable_405); // violet
    TGraph *refl_450 = new TGraph(n,x,yf5nr_stable_450); // blue
    TGraph *refl_505 = new TGraph(n,x,yt5nr_stable_505); // azure
    TGraph *refl_525 = new TGraph(n,x,yf5nr_stable_525); // green
    TGraph *refl_555 = new TGraph(n,x,ys5nr_stable_555); // yellow-green
    TGraph *refl_590 = new TGraph(n,x,ys5nr_stable_590); // yellow

    refl_450->SetTitle("Various Wavelength LEDs with 480nm Long Pass Dichroic Filter");
    refl_450->GetXaxis()->SetTitle("Incident Angle");
    refl_450->GetYaxis()->SetTitle("Percent Reflectance");
    refl_450->SetMaximum(101);
    refl_450->SetMinimum(0);
    refl_450->SetMarkerColor(kBlue);
    refl_450->SetMarkerStyle(21);
    refl_450->SetFillStyle(0);
    refl_450->SetFillColor(0);
    refl_385->SetMarkerColor(kBlue-8);
    refl_385->SetMarkerStyle(21);
    refl_385->SetFillStyle(0);
    refl_385->SetFillColor(0);
    refl_405->SetMarkerColor(kViolet);
    refl_405->SetMarkerStyle(21);
    refl_405->SetFillStyle(0);
    refl_405->SetFillColor(0);
    refl_505->SetMarkerColor(kAzure+1);
    refl_505->SetMarkerStyle(21);
    refl_505->SetFillStyle(0);
    refl_505->SetFillColor(0);
    refl_525->SetMarkerColor(kGreen);
    refl_525->SetMarkerStyle(21);
    refl_525->SetFillStyle(0);
    refl_525->SetFillColor(0);
    refl_555->SetMarkerColor(kSpring+6);
    refl_555->SetMarkerStyle(21);
    refl_555->SetFillStyle(0);
    refl_555->SetFillColor(0);
    refl_590->SetMarkerColor(kYellow);
    refl_590->SetMarkerStyle(21);
    refl_590->SetFillStyle(0);
    refl_590->SetFillColor(0);

    refl_450->Draw("ALP");
    refl_385->Draw("LP");
    refl_405->Draw("LP");
    refl_505->Draw("LP");
    refl_525->Draw("LP");
    refl_555->Draw("LP");
    refl_590->Draw("LP");

    c1->Update();

    TLegend *legend = new TLegend(0.1,0.7,0.3,0.9); // L,B,R,T 
    legend->AddEntry(refl_385, "385nm"); // light b/v
    legend->AddEntry(refl_405, "405nm"); // violet
    legend->AddEntry(refl_450, "450nm"); // blue
    legend->AddEntry(refl_505, "505nm"); // azure
    legend->AddEntry(refl_525, "525nm"); // green
    legend->AddEntry(refl_555, "555nm"); // green-yellow
    legend->AddEntry(refl_590, "590nm"); // yellow
    legend->SetTextFont(132);
    legend->SetFillColor(0);
    legend->SetFillStyle(0);
    legend->Draw();
    c1->Update();
}
