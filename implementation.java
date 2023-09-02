import java.util.*;
public class implementation{
    public static void JustPrint(){
        System.out.println(" ");
        System.out.println("1) LOW\n2) MEDIUM\n3) HIGH");
    }
    public static int getAvg(int a[], int n){
        int s=0;
        for(int i=0;i<n;i++){
            s+=a[i];
        }
        s/=n;
        return s;
    }
    public static int getSum(int a[]){
        int s=0;
        for(int i=0;i<a.length;i++)s+=a[i];
        return s;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("What are the number of employees working in your company: ");
        int size = sc.nextInt();
        int RaCC[] = new int[2];
        int F[] = new int[2];
        int P[] = new int[1];
        int SaH[] = new int[3];
        int FaLP[] = new int[2];
        int Priority[] = new int[5];
        
        //REPUTATION / CUSTOMER LOSS

        System.out.println("Enter choice 1 or 2 or 3");
        System.out.print("What is the reputation of the company/organization: ");
        JustPrint();
        RaCC[0] = sc.nextInt();
        System.out.print("Based on above reputation loss what is the category of customers that might lose the confidence in the company: ");
        JustPrint();
        RaCC[1] = sc.nextInt();
        
        //FINANCIAL
        System.out.print("Based on Operating Cost which category will the asset fall under: ");
        JustPrint();
        F[0] = sc.nextInt();
        System.out.print("What is the revenue loss that your company might incur if the asset is at risk: ");
        JustPrint();
        F[1] = sc.nextInt();
        
        //PRODUCTIVITY
        System.out.print("What is productive range of the organization based on staff working hours: ");
        JustPrint();
        P[0] = sc.nextInt();
        
        //SAFTY AND HEALTH
        System.out.print("How likely is the life of the employees at risk if the asset is attacked: ");
        JustPrint();
        SaH[0] = sc.nextInt();

        System.out.print("How likely is the health of the employees to be degraded if the asset is attacked: ");
        JustPrint();
        SaH[1] = sc.nextInt();

        System.out.print("How likely is the life of the employees at risk if the asset is attacked: ");
        JustPrint();
        SaH[2] = sc.nextInt();
        
        //FINES / LEGAL PENALITIES
        System.out.print("How likely is the company to bear Legal Fines: ");
        JustPrint();
        FaLP[0] = sc.nextInt();

        System.out.print("How much is the organization open to investigations from non-government, government and government or other organizations: ");
        JustPrint();
        FaLP[1] = sc.nextInt();

        //PRIORITY
        System.out.println("Prioritise respective *FIVE* impact areas: ");
        System.out.println("NOTE:- Higher the number higher the priority");
        System.out.print("Reputation and Customer Confidence: ");
        Priority[0] = sc.nextInt();
        System.out.print("Financial: ");
        Priority[1] = sc.nextInt();
        System.out.print("Productivity: ");
        Priority[2] = sc.nextInt();
        System.out.print("Safety and Health: ");
        Priority[3] = sc.nextInt();
        System.out.print("Fines and Legal Penalties: ");
        Priority[4] = sc.nextInt();

        //RISK CALCULATION

        int s=0;
        float fs=0;
        s=getAvg(RaCC,RaCC.length);
        fs+=Priority[0]*s; 
        s=getAvg(F,F.length);
        fs+=Priority[1]*s; 
        s=getAvg(P,P.length);
        fs+=Priority[2]*s; 
        s=getAvg(SaH,SaH.length);
        fs+=Priority[3]*s; 
        s=getAvg(FaLP,FaLP.length);
        fs+=Priority[4]*s; 

        System.out.println("The total risk is: "+fs);
        System.out.println("The percentage of risk is: "+(fs/(getSum(Priority)*3))*100+"%");




        

    }
}