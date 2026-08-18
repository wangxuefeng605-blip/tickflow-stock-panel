import {useStockScannerStore} from "@/lib/stockScannerStore"
import { api } from "@/lib/api"


export default function ScannerPanel(){

const {
 running,
 progress,
 results,
 start,
 updateProgress,
 finish
}=useStockScannerStore()


async function handleScan(){

  try {

    start()

    updateProgress(20)

    const data = await api.screenerRunPreset(
      "boll_breakout"
    )

    console.log("scanner result", data)

    updateProgress(80)


    finish(
      data.rows ?? []
    )


  } catch(e){

    console.error(
      "scanner failed",
      e
    )

    finish([])

  }

}



return (

<div className="p-6">


<h1 className="text-2xl font-bold">
AI 全盘扫描选股
</h1>


<button
onClick={handleScan}
disabled={running}
className="
mt-6
px-5
py-2
rounded-lg
bg-blue-500
text-white
"
>

{
running
?
"扫描中..."
:
"开始扫描"
}

</button>



<div className="mt-5">

扫描进度 {progress}%


<div
className="
h-2
bg-gray-700
rounded
mt-2
"
>

<div

style={{
width:`${progress}%`
}}

className="
h-full
bg-blue-500
rounded
"

/>


</div>

</div>




{
results.length > 0 && (

<div className="mt-6 space-y-3">


<h2 className="text-xl">
AI推荐股票
</h2>



{
results.map(stock=>(

<div

key={stock.symbol}

className="
p-4
rounded-xl
border
border-blue-500/30
bg-blue-500/10
flex
justify-between
"

>


<div>

<div>
{stock.name}
</div>


<div className="text-sm text-gray-400">

{stock.symbol}

</div>


</div>



<div className="text-blue-400">

AI {stock.score ?? "-"}

</div>


</div>


))

}


</div>

)

}


</div>

)

}