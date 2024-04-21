import React from "react";
import { LuSettings } from "react-icons/lu";
import User from "./user";
import CardUI from "./card";
import { Input } from "@/components/ui/input";
import { NavLinks } from "@/data/constants";
import { Link } from "react-router-dom";
import { Button } from "./ui/button";
import { Separator } from "@/components/ui/separator";
import { BiLogoCodepen } from "react-icons/bi";
const Sidebar: React.FC = () => {
  return (
    <aside className="w-full h-[100dvh] flex flex-col items-center justify-between bg-[#F9F9F9] subpixel-antialiased sticky top-0 py-6">
      <div className="text-5xl text-indigo-500 flex flex-row items-center">
        <BiLogoCodepen />
        <span className="text-4xl font-bold tracking-wide">Optimum</span>
      </div>
      <div className="flex flex-col items-left justify-evenly w-full gap-2 md:px-4">
        {NavLinks.map((navItem) => {
          return (
            <>
              <Link
                to={navItem.url}
                className="text-xl font-mediumbold links py-2 text-gray-600"
              >
                {navItem.name}
              </Link>
              <Separator />
            </>
          );
        })}
      </div>
      <CardUI
        headerComponent="Do you still need our help?"
        className="border-0 w-[90%] rounded-sm border-4 py-1 px-1"
        colorScheme={{
          bgColor: "bg-indigo-500",
          textColor: "text-white",
        }}
      >
        {/* <Input
          type="email"
          placeholder="Send us an email!"
          className="w-full mb-2"
        /> */}
        <Button
          type="submit"
          variant="secondary"
          className="text-indigo-600 font-bold text-2xl drop-shadow-lg"
        >
          Contact us
        </Button>
      </CardUI>
      <div className="flex items-center justify-between flex-row md:w-[90%]">
        <User imgHref="https://github.com/shadcn.png" fallBack="User profile" />
        <LuSettings className="w-[24px]" />
      </div>
    </aside>
  );
};
export default Sidebar;
