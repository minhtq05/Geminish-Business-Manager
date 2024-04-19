import React from "react";
import { LuSettings } from "react-icons/lu";
import { IoMdBusiness } from "react-icons/io";
import User from "./user";
import CardUI from "./card";
import { Input } from "@/components/ui/input";
import { NavLinks } from "@/data/constants";
import { Link } from "react-router-dom";
import { Button } from "./ui/button";
const Sidebar: React.FC = () => {
  return (
    <aside className="w-full h-full flex flex-col items-center justify-between bg-gray-50 subpixel-antialiased">
      <IoMdBusiness />
      <div className="flex flex-col items-left justify-evenly w-full gap-2 md:px-4">
        {NavLinks.map((navItem) => {
          return (
            <Link
              to={navItem.url}
              className="text-xl font-medium links py-2 text-gray-600"
            >
              {navItem.name}
            </Link>
          );
        })}
      </div>
      <CardUI
        heading="Do you still need our help?"
        className="border-0 w-[90%]"
        colorScheme={{
          bgColor: "bg-indigo-600",
          textColor: "text-white",
        }}
      >
        <Input
          type="email"
          placeholder="Send us an email!"
          className="w-full mb-2"
        />
        <Button type="submit">Submit</Button>
      </CardUI>
      <div className="flex items-center justify-between flex-row md:w-[90%]">
        <User imgHref="https://github.com/shadcn.png" fallBack="User profile" />
        <LuSettings className="w-[24px]" />
      </div>
    </aside>
  );
};
export default Sidebar;
