/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Praktikum;

/**
 *
 * @author MANGGAR-LAPTOP
 */
public class Latihan2 {
    public static void main(String[] args) {
        // penjumlahan matrik ordo dengan array
        int baris =(int) (1+Math.random()*10);
        int kolom =(int) (1+Math.random()*10);
        int [] [] matrik1 =new int [baris] [kolom];
        int [] [] matrik2 =new int [baris] [kolom];
        int [] [] matrik3 =new int [baris] [kolom];
        // inisialisasi kedua matrik
        
        for(int i =0; i<baris;i++){
            for(int j=0; j<kolom; j++){
                matrik1[i][j]=(int) (Math.random()*19-9);
                matrik2[i][j]=(int) (Math.random()*19-9);
            }
        }
        
        //proses penjumlahan matrik
        for(int i=0; i<baris; i++)
            for(int j=0; j<kolom; j++)
                matrik3[i][j] =matrik1[i][j]+matrik2[i][j];
            //cetak data matrik 1
        System.out.println("Data dari matriks 1");
        for(int i=0; i<matrik1.length; i++){
            System.out.print("\t");
            for(int j=0; j<matrik1[i].length; j++){
                if(matrik1[i][j]>=0)
                    System.out.print(" ");
                    System.out.print(matrik1[i][j]+" ");
                
            }
            System.out.println();
        }
        System.out.println();
        
        //cetak data matrik 2
        System.out.println("Data dari matriks 2");
        for(int i=0; i<matrik2.length; i++){
            System.out.print("\t");
            for(int j=0; j<matrik2[i].length; j++){
                if(matrik2[i][j]>=0)
                    System.out.print(" ");
                    System.out.print(matrik2[i][j]+" ");
                
            }
            System.out.println();
        }
        System.out.println();
        
        //mencetak hasil penjumlahan
        System.out.println("Matriks 3 Hasil Penjumlahan :");
        for(int i=0; i<matrik3.length; i++){
            System.out.print("\t");
            for(int j=0; j<matrik3[i].length; j++){
                if((matrik3[i][j]>-10) && (matrik3[i][j]<0))
                    System.out.print(" ");
                else
                    if((matrik3[i][j]>=0) && (matrik3[i][j]<10))
                    System.out.print(" ");
                else
                        if(matrik3[i][j]>=10)
                            System.out.print(" ");
                System.out.print(matrik3[i][j]+ " ");
                
            }
            System.out.println();
    }
        System.out.println();
}
}