import { motion } from "framer-motion"
import ExpandableComponent from "@/components/expandableContent"
import { Separator } from "@/components/ui/separator"
import User from "@/components/user";

interface SummaryPageProps{
    summaryText?:{ heading?: string; body: string },
}

const SummaryPage = ({summaryText} : SummaryPageProps) => {
    return(
        <div className="bg-[#F9F9F9] flex flex-col justify-start items-center gap-8 h-[100dvh] py-4 overflow-y-auto px-8" id="summary-container">
            {/* <Logo logoImg={<BiLogoCodepen/>} logoText={"Optimum"}/> */}
            <h1 className="text-4xl font-bold text-indigo-600">Summary</h1>
            <Separator/>
            <div className="w-full flex flex-row items-start justify-between gap-4">
                <User fallBack="Chatbot"/>
                <ExpandableComponent content={summaryText ? summaryText :{heading : "Chatbot is still gathering data for feedback, please come later", body : "Co cai cl ay dcmm"}} showsFull={true}/>
            </div>
        </div>
    )
}
export default SummaryPage;