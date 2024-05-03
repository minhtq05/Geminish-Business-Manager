import ExpandableComponent from "@/components/expandableContent";
import { Separator } from "@/components/ui/separator";
import User from "@/components/user";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import { Box } from "@mui/material";
import React, { useState, useEffect } from "react";
import customFetch from "@/utils/customFetch";
import CustomTabPanel from "@/components/customTabPanel";
import { SummaryDataType } from "@/data/types";
import CardUI from "@/components/card";
interface SummaryPageProps {
  summaryText?: { heading?: string; body: string };
}
interface ProductType {
  senders: string[];
  status: string[];
  summary: string[];
}

interface RawProductType {
  sender: string;
  products: {}[];
}

interface ProductReportsType {
  [key: string]: ProductType;
}
const SummaryPage = ({ summaryText }: SummaryPageProps) => {
  const [value, setValue] = useState(0);
  const [productList, setProductList] = useState<ProductReportsType>({});

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };
  const reformatData = (data: RawProductType[]): ProductReportsType => {
    const productReports: ProductReportsType = {};

    data.forEach((report: any) => {
      report.products.forEach((product: any) => {
        const productName = product.name;

        if (!productReports[productName]) {
          productReports[productName] = {
            senders: [],
            status: [],
            summary: [],
          };
        }

        productReports[productName].senders.push(report.sender);
        productReports[productName].status.push(product.status);
        productReports[productName].summary.push(...product.summary);
      });
    });

    return productReports;
  };
  const getSummaryData = async () => {
    try {
      const summaryRequest = await customFetch.get("/reports");
      // raw data

      const reformattedData = reformatData(summaryRequest.data.reports);
      setProductList(reformattedData);
    } catch (error) {
      console.log(`Error: ${error}`);
    }
  };
  useEffect(() => {
    getSummaryData();
  }, []);
  return (
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
          {Object.entries(productList).map(
            ([name, value]: [string, ProductType]) => {
              return <Tab key={name} label={name} />;
            }
          )}
        </Tabs>
      </Box>
      {Object.entries(productList).map(
        (
          [name, productData]: [name: string, productData: ProductType],
          index
        ) => {
          return (
            <CustomTabPanel key={name} value={value} index={index}>
              <div className="flex flex-col gap-4">
                {Object.entries(productData).map(
                  ([key, value]: [key: string, value: string[]]) => {
                    return (
                      <CardUI
                        colorScheme={{
                          bgColor: "bg-white",
                          textColor: "text-slate-600",
                        }}
                      >
                        <h1 className="text-2xl text-gray-700 font-bold my-2 break-all">
                          {key}
                        </h1>
                        <div className="flex flex-col gap-4">
                          {value.map((item: string, index: number) => {
                            return <p>{item}</p>;
                          })}
                        </div>
                      </CardUI>
                    );
                  }
                )}
              </div>
            </CustomTabPanel>
          );
        }
      )}
    </div>
  );
};
export default SummaryPage;
