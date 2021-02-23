#include <iostream>
#include <TGraph.h>
#include <TCanvas.h>
#include <TLegend.h>
using namespace std;

int sum_graph(){
    TCanvas *c1 = new TCanvas("c1","Simple Graph",700,500); // width & height

    const Int_t n = 12; // number of incidence angles; higher angles graze PMT

    Float_t x[n] = {15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0}; // array indexed by n; no refl less than 15 degrees

// Arrays of the sum of percent tranmission and reflection for each LED indexed by n

// 385nm LED
    Float_t sum_stable_385[n] = {24.894017475,48.349859533,75.0472015673,89.2745926347,90.2153359665,93.3430846651,96.5698498798,97.9053927188,97.7749845301,95.7532928619,93.2289486175,87.6219329863}; // of %T & %R

// 405nm LED
    Float_t sum_stable_405[n] = {30.22440505,71.40807399,86.33484315,95.34265538,100.2094686,93.29183638,97.71036203,100.5012179,100.2054681,88.15873659,98.67974449,96.95220674}; // of %T & %R

// 450nm LED
    Float_t sum_stable_450[n] = {50.1426834484,76.5955225796,92.3436364227,97.3422148248,98.095283833,95.1668681055,100.9564078037,101.2030798944,100.7944823492,99.9246134327,95.41828509,84.867671574}; // Sept 06

// 505nm LED
    Float_t sum_stable_505[n] = {93.5190189222,96.5570541898,98.4856735177,99.3814560466,97.6171602554,99.3720281928,97.2332210005,97.4051951938,97.6467881492,98.4218595858,98.9573498575,96.7056214983}; // of %T & %R

// 525nm LED
    Float_t sum_stable_525[n] = {89.932678415,99.4845244049,96.1335068458,96.9486437021,97.3608772877,96.4730141835,96.4273141354,96.9404601806,97.7166331074,97.3482299574,97.5828844668,94.0481311696}; // of %T & %R

// 555nm LED
    Float_t sum_stable_555[n] = {98.6908491598,97.9731851152,98.5186333438,99.4472944979,100.0131327096,99.9471360302,99.4617963381,98.8698753281,97.9417117771,97.225637164,92.0857938721,83.4556826633}; // of %T & %R

// 590nm LED
    Float_t sum_stable_590[n] = {92.8664073741,92.5002397619,95.3353885238,92.8658030906,92.7162740883,98.5001045924,98.8436061321,99.6326120089,96.229524696,92.0817643436,89.4681654463,79.916342619}; // of %T & %R

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
    legend->AddEntry(sum_385, "385nm October 25"); // light b/v
    legend->AddEntry(sum_405, "405nm October 10"); // violet
    legend->AddEntry(sum_450, "450nm September 6"); // blue
    legend->AddEntry(sum_505, "505nm September 12"); // azure
    legend->AddEntry(sum_525, "525nm September 12"); // green
    legend->AddEntry(sum_555, "555nm September 5"); // green-yellow
    legend->AddEntry(sum_590, "590nm September 20"); // yellow
    legend->SetTextFont(132);
    legend->SetFillColor(0);
    legend->SetFillStyle(0);
    legend->Draw();
    c1->Update();
}
