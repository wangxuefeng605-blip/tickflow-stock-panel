import { create } from "zustand"

interface ScannerState {
  running:boolean
  progress:number
  results:any[]
  start:()=>void
  updateProgress:(v:number)=>void
  finish:(data:any[])=>void
}

export const useStockScannerStore = create<ScannerState>((set)=>({

  running:false,

  progress:0,

  results:[],


  start(){
    set({
      running:true,
      progress:0,
      results:[]
    })
  },


  updateProgress(v){
    set({
      progress:v
    })
  },


  finish(data){
    set({
      running:false,
      progress:100,
      results:data
    })
  }

}))

