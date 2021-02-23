#include <iostream>
#include <TGraph.h>
#include <TCanvas.h>
#include <TLegend.h>
using namespace std;

int refl_graph(){
    TCanvas *c1 = new TCanvas("c1","Simple Graph",700,500); // width & height

    const Int_t n = 12; // number of incidence angles; higher angles graze PMT

    Float_t x[n] = {15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0}; // array indexed by n; no refl less than 15 degrees

// Arrays of percent reflections for each LED indexed by n
// yf5nr = y variable, f == first data point, 5 == 5 deg increments, n == n, r == reflection
// ys5nr = same, but s == second time through
// yt5nr = same, but t == third time through

// 385nm LED
    Float_t yf5nr_stable_385[n] = {24.7228033055,48.1608056469,74.9648071216,89.1680132701,90.1186694421,93.2165840513,96.4574034509,97.7328846349,97.5158785359,95.4261697024,92.8088902731,86.8875780757};

// 405nm LED
    Float_t yf5nr_stable_405[n] = {30.17660141,71.3677228,86.30467723,95.30069886,100.1656301,93.21657486,97.60564812,100.3316519,99.6925156,87.54272385,96.68762371,91.72794474};

// 450nm LED
    Float_t yf5nr_stable_450[n] = {49.2120381949,75.3859982815,90.702144858,94.7125532854,94.3947794088,88.7772924539,87.468723402,72.6646499223,60.8359650171,50.850088325,39.6964587563,24.3866885717};

// 505nm LED
    Float_t yt5nr_stable_505[n] = {17.2148651494,19.8569949445,19.0235396277,15.5272120553,12.4472005159,10.0756384746,9.1520366306,9.1232655377,9.6273783139,11.5777481495,14.0407561947,16.8939727671};

// 525nm LED
    Float_t yf5nr_stable_525[n] = {1.3088549838,6.5571581444,7.2843255179,7.5421605025,7.7376638041,8.0052576036,8.3447959043,8.8282703537,9.5597308274,10.1171225618,11.7977008534,14.0171765016};

// 555nm LED
    Float_t ys5nr_stable_555[n] = {1.7585300943,3.8949187137,4.8540163702,5.2116676832,5.5073532524,5.58343816,5.8783599227,6.3804411879,7.9068821817,8.7223092869,9.0503907612,4.9662651436};

// 590nm LED
    Float_t ys5nr_stable_590[n] = {2.0719838891,3.6253165076,4.918945339,4.6444271162,4.9356233645,5.4665827259,5.9528114775,7.1487447702,7.5440064319,8.5496935002,11.0662898772,12.883149515};

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
    legend->AddEntry(refl_385, "385nm October 25"); // light b/v
    legend->AddEntry(refl_405, "405nm October 10"); // violet
    legend->AddEntry(refl_450, "450nm September 6"); // blue
    legend->AddEntry(refl_505, "505nm September 12"); // azure
    legend->AddEntry(refl_525, "525nm September 12"); // green
    legend->AddEntry(refl_555, "555nm September 5"); // green-yellow
    legend->AddEntry(refl_590, "590nm September 20"); // yellow
    legend->SetTextFont(132);
    legend->SetFillColor(0);
    legend->SetFillStyle(0);
    legend->Draw();
    c1->Update();
}
