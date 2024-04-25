import React from "react";
import { LuSettings } from "react-icons/lu";
import User from "./user";
import CardUI from "./card";
import { NavLinks } from "@/data/constants";
import { Link } from "react-router-dom";
import { Button } from "./ui/button";
import { Separator } from "@/components/ui/separator";
import { BiLogoCodepen } from "react-icons/bi";
import { GoChevronDown } from "react-icons/go";
import NavItem from "./navItem";
import Logo from "./logo";
const Sidebar: React.FC = () => {
  return (
    <aside className="w-[fit-content] h-[100dvh] flex flex-col items-center justify-between bg-[#F9F9F9] subpixel-antialiased py-4">
      <Logo logoImg={<BiLogoCodepen />} logoText={"Optimum"} />
      <div className="flex flex-col items-left justify-evenly w-full gap-2 md:px-2">
        {NavLinks.map((navItem) => {
          return (
            // <>
            //   <Link
            //     to={navItem.url}
            //     className="text-xl font-mediumbold links py-2 text-gray-600"
            //   >
            //     {navItem.name}
            //   </Link>
            //   <Separator />
            // </>
            <NavItem
              icon={<GoChevronDown />}
              isSeperated={true}
              url={navItem.url}
              name={navItem.name}
            />
          );
        })}
      </div>
      <CardUI
        headerComponent="Do you still need our help?"
        className="border-0 w-[90%] rounded-sm border-4 py-1 px-1"
        colorScheme={{
          bgColor: "linear-color-background",
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
      <div className="flex items-center justify-between flex-row md:w-[90%] border-2 border-slate-400 p-2 rounded-md">
        <User imgHref="https://github.com/shadcn.png" fallBack="User profile" />
        <LuSettings className="w-[24px]" />
      </div>
    </aside>
  );
};
export default Sidebar;
