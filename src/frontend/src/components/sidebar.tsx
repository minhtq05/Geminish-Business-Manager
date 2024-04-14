import React from "react";
import { LuSettings } from "react-icons/lu";
import { IoMdBusiness } from "react-icons/io";
import User from "./user";
import CardUI from "./card";
import { Input } from "@/components/ui/input"
import { NavLinks } from "@/data/constants";
import {Link} from "react-router-dom"
import { Button } from "./ui/button";
const Sidebar:React.FC = () => {
    return(
        <aside className="w-full h-full flex flex-col items-center justify-between">
            <IoMdBusiness />
            <div className="flex flex-col items-center justify-evenly">
                {NavLinks.map(navItem => {
                    return(
                        <Link to={navItem.url} className="block">{navItem.name}</Link>
                    )
                })}
            </div>
            <CardUI heading="Do you still need our help?" subheading="Feel free to send us a request!" className="border-0">
                <Input type="email" placeholder="Enter your email" className="w-full"/>
                <Button variant="outline">Submit</Button>
            </CardUI>
            <div className="flex items-center justify-between flex-row">
                <User imgHref="https://github.com/shadcn.png" fallBack="User profile"/>
                <LuSettings/>
            </div>
        </aside>
    )
}
export default Sidebar;