import { motion } from "framer-motion";
import ExpandableComponent from "@/components/expandableContent";
import { Separator } from "@/components/ui/separator";
import User from "@/components/user";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import { Box } from "@mui/material";
import React, { useState } from "react";

import CustomTabPanel from "@/components/customTabPanel";

interface SummaryPageProps {
  summaryText?: { heading?: string; body: string };
}

const SummaryPage = ({ summaryText }: SummaryPageProps) => {
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    // <div className="bg-[#F9F9F9] flex flex-col justify-start items-center gap-8 h-[100dvh] py-4 overflow-y-auto px-8" id="summary-container">
    //     {/* <Logo logoImg={<BiLogoCodepen/>} logoText={"Optimum"}/> */}
    //     <h1 className="text-4xl font-bold text-indigo-600">Summary</h1>
    //     <Separator/>
    //     <div className="w-full flex flex-row items-start justify-between gap-4">
    //         <User fallBack="Chatbot"/>
    //         <ExpandableComponent content={summaryText ? summaryText :{heading : "Chatbot is still gathering data for feedback, please come later", body : "Co cai cl ay dcmm"}} showsFull={true}/>
    //     </div>
    // </div>
    <div
      className="bg-[#F9F9F9] flex flex-col justify-start items-stretch gap-8 h-[100dvh] py-4 overflow-y-auto px-8"
      id="summary-container"
    >
      <h1 className="text-4xl font-bold text-indigo-600 text-center">
        Summary
      </h1>
      <Separator />
      <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
        <Tabs
          value={value}
          onChange={handleChange}
          aria-label="basic tabs example"
        >
          <Tab label="Item One" />
          <Tab label="Item Two" />
          <Tab label="Item Three" />
        </Tabs>
      </Box>
      <CustomTabPanel value={value} index={0}>
        <User fallBack="Chatbot" />{" "}
        <ExpandableComponent
          content={
            summaryText
              ? summaryText
              : {
                  heading:
                    "Chatbot is still gathering data for feedback, please come later",
                  body: "Co cai cl ay dcmm",
                }
          }
          showsFull={true}
        />
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        <User fallBack="Chatbot" />{" "}
        <ExpandableComponent
          content={
            summaryText
              ? summaryText
              : {
                  heading:
                    "Chatbot is still gathering data for feedback, please come later",
                  body: "Co cai cl ay dcmm",
                }
          }
          showsFull={true}
        />
      </CustomTabPanel>
      <CustomTabPanel value={value} index={2}>
        <User fallBack="Chatbot" />{" "}
        <ExpandableComponent
          content={
            summaryText
              ? summaryText
              : {
                  heading:
                    "Chatbot is still gathering data for feedback, please come later",
                  body: "Co cai cl ay dcmm",
                }
          }
          showsFull={true}
        />
      </CustomTabPanel>
    </div>
  );
};
export default SummaryPage;
