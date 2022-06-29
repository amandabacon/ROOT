#include <iostream>
#include <TGraph.h>
#include <TCanvas.h>
#include <TLegend.h>
using namespace std;

int sum_graph(){
    TCanvas *c1 = new TCanvas("c1","Simple Graph",700,500); // width & height

    const Int_t n = 12; // remove 75 and 80 degrees due to grazing

    Float_t x[n] = {15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0};

// 385nm
    Float_t sum_stable_385[n] = {}; // of %T & %R

// 405nm
    Float_t sum_stable_405[n] = {}; // of %T & %R

// 450nm
    Float_t sum_stable_450[n] = {}; // of %T & %R

// 505nm
    Float_t sum_stable_505[n] = {}; // of %T & %R

// 525nm
    Float_t sum_stable_525[n] = {}; // of %T & %R

// 555nm
    Float_t sum_stable_555[n] = {}; // of %T & %R

// 590nm
    Float_t sum_stable_590[n] = {}; // of %T & %R

    c1->SetGrid();

    TGraph *sum_385 = new TGraph(n,x,sum_stable_385); // light b/v
    TGraph *sum_405 = new TGraph(n,x,sum_stable_405); // violet
    TGraph *sum_450 = new TGraph(n,x,sum_stable_450); // blue
    TGraph *sum_505 = new TGraph(n,x,sum_stable_505); // azure
    TGraph *sum_525 = new TGraph(n,x,sum_stable_525); // green
    TGraph *sum_555 = new TGraph(n,x,sum_stable_555); // yellow-green
    TGraph *sum_590 = new TGraph(n,x,sum_stable_590); // yellow

    sum_450->SetTitle("Various Wavelength LEDs with 480nm Long Pass Dichroic Filter");
    sum_450->GetXaxis()->SetTitle("Incident Angle");
    sum_450->GetYaxis()->SetTitle("Sum");
    sum_450->SetMaximum(102);
    sum_450->SetMinimum(0);
    sum_450->SetMarkerColor(kBlue);
    sum_450->SetMarkerStyle(21);
    sum_450->SetFillStyle(0);
    sum_450->SetFillColor(0);
    sum_385->SetMarkerColor(kBlue-8);
    sum_385->SetMarkerStyle(21);
    sum_385->SetFillStyle(0);
    sum_385->SetFillColor(0);
    sum_405->SetMarkerColor(kViolet);
    sum_405->SetMarkerStyle(21);
    sum_405->SetFillStyle(0);
    sum_405->SetFillColor(0);
    sum_505->SetMarkerColor(kAzure+1);
    sum_505->SetMarkerStyle(21);
    sum_505->SetFillStyle(0);
    sum_505->SetFillColor(0);
    sum_525->SetMarkerColor(kGreen);
    sum_525->SetMarkerStyle(21);
    sum_525->SetFillStyle(0);
    sum_525->SetFillColor(0);
    sum_555->SetMarkerColor(kSpring+6);
    sum_555->SetMarkerStyle(21);
    sum_555->SetFillStyle(0);
    sum_555->SetFillColor(0);
    sum_590->SetMarkerColor(kYellow);
    sum_590->SetMarkerStyle(21);
    sum_590->SetFillStyle(0);
    sum_590->SetFillColor(0);

    sum_450->Draw("ALP");
    sum_385->Draw("LP");
    sum_405->Draw("LP");
    sum_505->Draw("LP");
    sum_525->Draw("LP");
    sum_555->Draw("LP");
    sum_590->Draw("LP");

    c1->Update();

    TLegend *legend = new TLegend(0.7,0.5,0.9,0.7); // L,B,R,T 
    legend->AddEntry(sum_385, "385nm"); // light b/v
    legend->AddEntry(sum_405, "405nm"); // violet
    legend->AddEntry(sum_450, "450nm"); // blue
    legend->AddEntry(sum_505, "505nm"); // azure
    legend->AddEntry(sum_525, "525nm"); // green
    legend->AddEntry(sum_555, "555nm"); // green-yellow
    legend->AddEntry(sum_590, "590nm"); // yellow
    legend->SetTextFont(132);
    legend->SetFillColor(0);
    legend->SetFillStyle(0);
    legend->Draw();
    c1->Update();
}
